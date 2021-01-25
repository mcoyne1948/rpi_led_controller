# rpi_led_ctrl
A Naomi speech handler plugin for controlling LEDs on a remote Raspberry Pi using gRPC
- **Language** English
- **Naomi Version Support** V3.0
- **Dependencies** gRPC, Python wiringpi
## Description
Naomi acts as a client collecting vocal input about the colour(s) and operation to be performed on a red and green LEDs connected to the GPIO port of a remote Raspberry Pi. It communicates via gRPC with a server on the remote Raspberry Pi which uses the python wiringpi access routines to actually contol the pins the LEDs are connected to.
## Install
Installation is an involved process reqiring 
### Prerequisites
Client requires the gRPC module which the server requires the both the gRPC and Python wiringpi modules.
### Install Client
### Install Server
