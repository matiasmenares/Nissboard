#!/bin/bash
xset s noblank
xset s off
xset -dpms

unclutter -idle 0.5 -root &

sed -i 's/"exited_cleanly":false/"exited_cleanly":true/' /home/pi/.config/chromium/Default/Preferences
sed -i 's/"exit_type":"Crashed"/"exit_type":"Normal"/' /home/pi/.config/chromium/Default/Preferences

/usr/bin/chromium-browser --noerrdialogs --disable-pinch --overscroll-history-navigation=0  --incognito --disable-infobars --kiosk http://localhost &

/usr/bin/python3 /home/pi/nissboard-prod/dash.py -d /dev/ttyUSB0 -g /dev/ttyUSB0 -a /dev/ttyACM0 &amp;

#while true; do
#   xdotool keydown ctrl+Tab; xdotool keyup ctrl+Tab;
#   sleep 10
#done