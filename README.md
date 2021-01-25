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
