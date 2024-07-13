#!/bin/sh

while [ 1 ]; do
	echo "Starting python LEDClock (Advanced)"
	sudo rfkill unblock bluetooth
	cd /home/pi/neoclock
	. /home/pi/.env/bin/activate
	python clock_adv.py
	#python /home/pi/pirate-audio/examples/rainbow.py
	#python /home/pi/pirate-audio/examples/buttons.py
	echo "LEDClock (Advanced) stopped, restarting"
	sleep 1
done
