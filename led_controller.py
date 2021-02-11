# This plugin is the Naomi client for a server that runs on a remote process,
# typically on a different Raspberry Pi, which controls the behaviour of two.
# LEDs in response of Naomi voice commands. Both ends use the protocol buffer
# based gRPC classes to handle communication between the client and server
# process. The server end also makes use of the Python wiringpi classes to access
# the GPIO pins controlling the LEDs.

#import serial
from naomi import plugin
from naomi import profile

# gRPC imports
import logging
import grpc
from .led_responder import led_ctlr_pb2
from .led_responder import led_ctlr_pb2_grpc

class ControlLEDPlugin(plugin.SpeechHandlerPlugin):
    
    warning_msg = ""
    serverIP = '192.168.50.173:50051'

    LED = [0, 0]
    GREEN = 0		# Following are the colour options
    RED = 1
    BOTH = 2
    OFF = 0		# Following are the LED control options
    NOERROR = 0		# Default to LED off
    ON = 1
    BLINK = 2
    ERROR = 3

    def intents(self):
        return {
            'LEDIntent': {
                'locale': {
                    'en-US': {
                        'keywords': {
                            'LEDThingKeyword': [
                                'LED',
                                'ELLEEDEE',
                                'LIGHT'
                            ],
                            'LEDColorKeyword': [
                                'RED',
                                'GREEN'
                            ],
                            'LEDOperationKeyword': [
                                'ON',
                                'OFF'
                            ],
                            'LEDActionKeyword': [
                                'SET',
                                'TURN',
                                'BLINK'
                            ]
                        },
                        'templates': [
                            "{LEDActionKeyword} THE {LEDColorKeyword} {LEDThingKeyword} {LEDOperationKeyword}",
                            "{LEDActionKeyword} {LEDOperationKeyword} THE {LEDColorKeyword} {LEDThingKeyword}"
                            "{LEDActionKeyword} THE {LEDColorKeyword} {LEDThingKeyword}"
                            "{LEDActionKeyword} {LEDColorKeyword} {LEDThingKeyword}"
                        ]
                    },
                    'fr-FR': {
                        'keywords': {
                            'LEDThingKeyword': [
                                'ELLEEDEE',
                                'LUMIERE'
                            ],
                            'LEDColorKeyword': [
                                'ROUGE',
                                'VERTE'
                            ],
                            'LEDOperationKeyword': [
                                'ALLUME',
                                'ETEINT'
                            ]
                        },
                        'templates': [
                            "{LEDOperationKeyword} LA {LEDThingKeyword} {LEDColorKeyword}"
                        ]
                    }
                },
                'action': self.handle
            }
        }

    def handle(self, intent, mic):
        """
        Once the brain detected the keywords above,
        it trigger this part
        """

        # Naomi 3.0+
        # Check for control inputs
        try:
            COLOR = intent['matches']['LEDColorKeyword'][0]
        except KeyError:
            COLOR = None
        try:
            OPERATION = intent['matches']['LEDOperationKeyword'][0]
        except KeyError:
            OPERATION = None
        try:
            ACTION = intent['matches']['LEDActionKeyword'][0]
        except KeyError:
            ACTION = None

        #
        #
        #
        #
        actCrtl = self.NOERROR  # Set no error
        if ACTION is None or ACTION == "NAOMI":		# Handle no ACTION input
            ACTION = 'TURN'
        if ACTION == 'BLINK':				# Set control parameters for blink
            actCrtl = self.BLINK
            if COLOR == 'GREEN':
                colr = self.GREEN
            elif COLOR == 'RED':
                colr = self.RED
            else:
                # Blink both color LED off-on-off
                colr = self.BOTH
        elif ACTION == 'TURN' or ACTION == 'SET':	# Set control parameters for change LED state
            if COLOR == 'GREEN':
                colr = self.GREEN
                if OPERATION == "ON" or OPERATION is None:
                    actCrtl = self.ON
                else:
                    actCrtl = self.OFF
            elif COLOR == 'RED':
                colr = self.RED
                if OPERATION == "ON" or OPERATION is None:
                    actCrtl = self.ON
                else:
                    actCrtl = self.OFF
            else:					# No colour defined in input
                colr = self.BOTH
                if OPERATION == "ON":
                        actCrtl = self.ON
                elif OPERATION == "OFF":
                        actCrtl = self.OFF
                else:
                    # Can't detect action default to on
                    actCrtl = self.ON
        else:
            actCrtl = self.ERROR    # Set error

        if actCrtl == self.ERROR:
            mic.say(self.gettext("Error: could not determine action to take!"))
        else:
            # print("LED controller: %d, %d" %(actCrtl,colr))	# Debug code

            # Send LED change control message to server
            ans_text = "RPi LED Controller"
            channel = grpc.insecure_channel(serverIP)
            stub = led_ctlr_pb2_grpc.RPi_CtlrStub(channel)
            response = stub.SendMsg(led_ctlr_pb2.RPiRequest(name=ans_text, colour=colr, operation=actCrtl))

            # Deal with response from server
            print("LED controller client received: " + response.message)
            fmt = self.gettext(response.message)
            mic.say(fmt)
