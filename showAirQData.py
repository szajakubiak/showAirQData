#!/usr/bin/python3

# Import modules
import csv, serial
from random import randrange
from time import sleep
from font_pl import font

# Initialize serial port
s = serial.Serial()
s.baudrate = 9600
s.timeout = 0
s.port = '/dev/ttyACM0'
s.open()

# Read air quality data from file
with open('airQData.txt', 'r') as dataFile:
    dataFileReader = csv.reader(dataFile)
    data = []
    for row in dataFileReader:
        # Select only data line which will scroll under 45 sec
        if len(row[0]) <= 120:
            data = data + [row]
dataFile.close()

# Helper function to transmit quote char by char
def transmission(message):
	# Message header for Pi-Lite
	header = '$$$F'
	
	# Transmission delay
	transmission_delay = 0.001
	
	# Letters separator
	separator = '000000000'
	
	# Add 7 spaces at the end of the message to clear the screen
	# after transmission
	message += 7 * ' '
	
	# Wariable which stores screen pixel states
	# (0 is off, 1 is on)
	screen = ''
	for i in range(126):
		screen += '0'
	for i in range(len(message)):
		# Create buffer for char i pixels
		buf = font[message[i]] + separator
		while len(buf) > 0:
			# Delete leftmost column from screen
			screen = screen[9:]
			# Append leftmost column from buffer as rightmost column on screen
			screen += buf[:9]
			# Remove appended column from buffer
			buf = buf[9:]
			s.write ((header + screen  + '\r\n').encode())
			sleep(transmission_delay)

# Select random data line
line = data[randrange(len(data))][0]
# Transmit selected line
transmission(line)

s.close()
