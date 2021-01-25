# rpi_led_ctrl
A simple module that combine Naomi and a separate Raspberry Pi platform to show possibilities in IOT and new interactions.  
A Naomi speech handler plugin for controlling two LEDs attached to the pins of the GPIO connector on a remote network connected Raspberry Pi.
- **Language** English
- **Naomi Version Support** V3.0
- **Dependencies** gRPC, Python wiringpi
## Description
Naomi acts as a client collecting vocal input about the colour(s) and operation to be performed on a red and green LEDs connected to pins of the GPIO port on a remote network connected Raspberry Pi acting as the server. The inter-platform communicates is handled using Googles open source protocol buffer mechanism implemented via the gRPC module. The server on the remote Raspberry Pi makes use of the python wiringpi module to access the GPIO port and contol the pins the LEDs are connected to.
## Install
Installation is an involved process. On the client it requires not just installing and enabling the rpi_led_ctrl plugin using Naomi commands but also the installation of the gRPC module. On server the server-side software, the gRPC module, the rpi_led_ctrl gRPC classes  and Python wiringpi module must all be installed.
### Install Client

### Install Server
gRPC
Python server program
#### Wiring

## Going Further
- **Change GPIO Pins** The default assignment of the green LED on GPIO20, physical connector pin 38, and the red LED on GPIO21, physical pin 40. 
The actual GPIO pins used can easily be changed by modifying the values of **greenGPIOpin** and/or **redGPIOpin**
near the beginning of the file **led_ctlr_server.py** but this will of course change the physical pin assignment on the connector.
- **Add message features to protocol buffer channel** - Features are added to the communication channel as defined  by the gRPC protocol buffer specifications in the led_ctlr.proto file included with the server software. A basic tutorial on the definition and use of this file can be found in the [Quick start](https://grpc.io/docs/languages/python/quickstart/) for gRPC.
- **Add new remote control functions** - The possibilities are endless. There are many I2C sensors for tempurature, humidity, air pressure, magnetometer, accelerometer, gyroscopes, etc. that are easily interfaced with a Raspberry Pi and therefore could be made accessible to Naomi.
