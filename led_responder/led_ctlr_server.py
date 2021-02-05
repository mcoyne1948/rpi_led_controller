# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# The Python implementation of the GRPC RPI LED server."""

from concurrent import futures
import logging

import time

import grpc			# Remote Procedure Call classes
import wiringpi			# GPIO access and control classes

import led_ctlr_pb2		# RPC classes using google potocol buffers
import led_ctlr_pb2_grpc	# to implement both client and server sides

# A bunch of constants to help with code readability
greenGPIOpin = 20	# Actual RPi GPIO number for green LED
redGPIOpin = 21		# Actual RPi GPIO number for red LED
bothGPIOpins = -1	# Magic number to indicate both GPIO pin
GreenColour = 0		# Colour green LED
RedColour = 1		# Colour red LED
BothColour = 2		# Both LED colours
OffOp = 0		# LED Off operation
OnOp = 1		# LED On operation
BlinkOp = 2		# LED blink operation

class RPi_Ctlr(led_ctlr_pb2_grpc.RPi_CtlrServicer):

    # Server side code to handle the inputs from the Naomi client
    def SendMsg(self, request, context):

        # Debug stuff to check communications
        if request.colour == GreenColour:      ColourIs = "Green"
        elif request.colour == RedColour:      ColourIs = "Red"
        else:                                  ColourIs = "Both"
        if request.operation == OffOp:         OperationIs = "Off"
        elif request.operation == OnOp:        OperationIs = "On"
        else:                                  OperationIs = "Blink"
        print("Following Naomi request recieved: %s LED %s" % (ColourIs, OperationIs))

        # Code to handle LED operations
        replayMsg = "SUCCESSFUL"
        # First map LED colour to corresponding GPIO pin number
        if request.colour == GreenColour:
            GPIOpin = greenGPIOpin	# Green LED GPIO pin
        elif request.colour == RedColour:
            GPIOpin = redGPIOpin	# Red LED GPIO pin
        else:
            GPIOpin = bothGPIOpins	# Both LED GPIO pin

        if request.colour == BothColour and request.operation == BlinkOp: # Blink both LEDs
            self.BlinkLED(GPIOpin, request.colour)
        elif request.colour == BothColour:			# Change both LEDs
            self.ChangeLED (redGPIOpin, request.operation)
            self.ChangeLED (greenGPIOpin, request.operation)
        elif request.operation == OffOp:			# LED Off
            self.ChangeLED (GPIOpin, OffOp)
        elif request.operation == OnOp:				# LED On
            self.ChangeLED (GPIOpin, OnOp)
        elif request.operation == BlinkOp:			# Blink one LED
            self.BlinkLED(GPIOpin, request.colour)
        else:
            replayMsg = "FAILED"

        return led_ctlr_pb2.RPiReply(message='LED OPERATION, %s!' % replayMsg)

    def ChangeLED(self, GPIOpin, change):
        wiringpi.digitalWrite (GPIOpin, change)

    def BlinkLED(self, GPIOpin, numLEDs):
        if GPIOpin == bothGPIOpins:			# Blink alternating LED colours
            for x in range(3):				# Arbitrarily blink 3 times
                wiringpi.digitalWrite (greenGPIOpin, OffOp)
                wiringpi.digitalWrite (redGPIOpin, OnOp)
                time.sleep(1)
                wiringpi.digitalWrite (greenGPIOpin, OnOp)
                wiringpi.digitalWrite (redGPIOpin, OffOp)
                time.sleep(0.5)
            wiringpi.digitalWrite (redGPIOpin, OffOp)	# Ensure all LEDs off	
            wiringpi.digitalWrite (greenGPIOpin, OffOp)
        else:						# Blink a single LED
            for x in range(3):				# Arbitrarily blink 3 times
                wiringpi.digitalWrite (GPIOpin, OnOp)
                time.sleep(1)
                wiringpi.digitalWrite (GPIOpin, OffOp)
                time.sleep(0.5)

# Set up wiringPi for GPIO pin control and gRPC for communication with the
# Naomi client (Note: Client/server communication is insecure, see gRPC 
# documentation if you need to make the link secure.)
def serve():
    print("Start RPi LED Responder server")
    wiringpi.wiringPiSetupGpio()	# Initialize GPIO interface access
    wiringpi.pinMode(greenGPIOpin, 1)	# GPIO pin, mode=1 (output) Green LED
    wiringpi.pinMode(redGPIOpin, 1)	# GPIO pin, mode=1 (output) Red LED
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    led_ctlr_pb2_grpc.add_RPi_CtlrServicer_to_server(RPi_Ctlr(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
