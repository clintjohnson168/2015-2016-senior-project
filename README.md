# senior-project
Senior Project - Smart Mailbox

This Device uses Debian GNU/Linux 7

Hardware:
	push buttions are connected to 2 of the Beaglebone's GPIO pins. 
	one setup as a power output, and the other set up as an input sensor 

Core program code:
	Written in python in the file PIR_Message.py. This file creates sensor objects, and 
	goes into a loop to check and see if a sensor has been actavated. If triggered, it will send a text
	to the correct mailbox owner. 

Launcher program script to run PIR_Message.py at startup
  Uses launcher.sh
