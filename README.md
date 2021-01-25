# rpi_led_ctrl
A Naomi speech handler plugin for controlling LEDs on a remote Raspberry Pi using gRPC
##Description
Naomi acts as a client collecting vocal input about the colour(s) and operation to be performed on a red and green LEDs connected to the GPIO port of a remote Raspberry Pi. It communicates via gRPC with a server on the remote Raspberry Pi which uses the python wiringpi access routines to actually contol the pins the LEDs are connected to.
##Install
