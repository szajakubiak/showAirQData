# showAirQData

Display air quality data on the Pi-Lite LED matrix.

## Detailed description

This script is meant to be used with **getAirQData** script (available in a separate repository), which creates **airQData.txt** file with current values of PM2.5 and PM10 from selected measuring stations. Script should be run on a Raspberry Pi with a 9 x 14 LED matrix called Pi-Lite connected. Pi-Lite users' guide can be found [here](http://www.spiratronics.com/data/A911.pdf). A compatible clone may also be used. Some tutorials on how to use the Pi-Lite with a Raspberry Pi can be found [here](https://www.raspberrypi-spy.co.uk/?s=pi-lite).

## Dependencies

Besides Python 3 pyserial library needs to be installed:

    pip install pyserial
