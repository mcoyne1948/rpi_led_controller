# rpi_led_ctrl
A simple module that combine Naomi and a separate Raspberry Pi platform to show possibilities in IOT and new interactions.  
This Naomi speech handler plugin implements the control of two LEDs attached to the pins of the GPIO connector on a remote network connected Raspberry Pi. Under voice control either or both LEDs can be turned on or off or blinked.
- **Language** English
- **Naomi Version Support** V3.0
- **Dependencies** gRPC, Python wiringpi
## Description
In this plugin Naomi acts as a client collecting vocal input about the colour(s) and operation to be performed on a red and green LEDs connected to pins of the GPIO port physical connector on a remote network connected Raspberry Pi acting as the server. The inter-platform communicates is handled using Googles open source protocol buffer mechanism implemented via the gRPC module. The server on the remote Raspberry Pi makes use of the Python wiringpi module to access the GPIO port and electrically contol the pins the LEDs are connected to.
## Install
Installation is an involved process since there is separate software that must be install on both the client and server. On the client it requires not just installing and enabling the rpi_led_ctrl plugin using Naomi commands but also gRPC module must be installed. On server the server-side controller software, the gRPC module, the rpi_led_ctrl gRPC classes  and Python wiringpi module must all be installed.
### Install Client
The rpi_led_ctrl plugin is installed in Naomi as follows:
```shell
cd your_Naomi_directory
./Naomi --install "led_contoller"  
...  
./Naomi --enable "led_contoller"  
...  
```
Instructions for the installation of the gRPC module may be found [here](https://grpc.io/docs/languages/python/quickstart/). This should be done as root using sudo. (**Note**: You only need to install the grpcio-tools if you make chanes to the .proto file and need to recompile it.)
### Install Server
Instructions for the installation of the gRPC module may be found above.  
Instructions for the installation of the Python wiringpi module may be found [here](https://pypi.org/project/wiringpi/).
The directory containing the led controller server program should be copied to an appropriate location in the home directory.
#### Wiring

## Operation and Testing
With all the software installed on both client and server, and the hardware setup on the server, start the Naomi client:
```shell
cd your_Naomi_directory
./Naomi --install "led_contoller"    
```
Then go to a terminal session on the Raspberry Pi LED controller server and enter:
```shell
cd led_controller_server_program_directory
./led_controller.py 
```

## Going Further
- **Change GPIO Pins** The default assignment of the green LED on GPIO20, physical connector pin 38, and the red LED on GPIO21, physical pin 40. 
The actual GPIO pins used can easily be changed by modifying the values of **greenGPIOpin** and/or **redGPIOpin**
near the beginning of the file **led_ctlr_server.py** but this will of course change the physical pin assignment on the connector.
- **Add message features to protocol buffer channel** - Features are added to the communication channel as defined  by the gRPC protocol buffer specifications in the led_ctlr.proto file included with the server software. A basic tutorial on the definition and use of this file can be found in the [Quick start](https://grpc.io/docs/languages/python/quickstart/) and [Basic Tutorial](https://grpc.io/docs/languages/python/basics/) for gRPC.
- **Add new remote control functions** - The above application makes use of the Python port of the wiringpi libraries for the server which were originally develop for C. Unfortunately the original author, after ten years of support, has decided to move on and deprecated the original libraries. This currently effects mostly the accuracy of some of the documentation at [wiringpi site](http://wiringpi.com/). However the good news is that the original project has been forked and is supported by a new community.  
This all being said the wiringpi suite of capabilities is available and supports access to a variety of GPIO functionality. In particular, for example, there are many I2C sensors for tempurature, humidity, air pressure, magnetometer, accelerometer, gyroscopes, etc. that are easily interfaced with a Raspberry Pi using [I2C wiringpi routines](http://wiringpi.com/reference/i2c-library/) and therefore could be made accessible to Naomi. The development of this kind of gRPC and wiringpi functionality is beyond the realm of Naomi user support and developers are directed to the communities supporting these specific packages.
