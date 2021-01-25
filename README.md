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
The default assignment of the green LED on GPIO20, physical connector pin 38, and the red LED on GPIO21, physical pin 40. 
The actual GPIO pins used can easily be changed by modifying the values of **greenGPIOpin** and/or **redGPIOpin**
near the beginning of the file **led_ctlr_server.py** but this will of course change the physical pin assignment on the connector.
##Going Further
- **Change GPIO Pins**
- **Add message features to protocol buffer channel**
- **Add new remote control functions**
