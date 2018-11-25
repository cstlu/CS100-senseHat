#! /usr/bin/env python

# sense_hat_clock ------ By Cathal Stewart Sept 2016 edited to sense_clock_new Nov 2016
# 
# Raspberry Pi from - http://www.raspberrypi.org/
#
#
#
# Import moduals and define function

from sense_hat import SenseHat
import time, os, sys
from time import localtime, strftime


sense = SenseHat()
#sense.set_rotation(180)

repeat = 2
txt_scroll_speed =0.085
frame_delay = 0.09
pause_delay = 2
min_flash = 20


# Get hour and min numbers
time_h = strftime("%I", localtime())
time_m = strftime("%M", localtime())
time_h_24h = strftime("%H", localtime())

# Get time and date to display
time_d = strftime(" - On - %A %B %d %Y", localtime())
ampm = strftime(" %p", localtime())
time_flash = ' *** ' + time_h_24h + ':' + time_m



# Set colour values to hours
if time_h == '01':
	hour_colour = 255,255,255 # white
	htext = 'One'
elif time_h == '02':
	hour_colour = 255,127,0 # orange
	htext = 'Two'
elif time_h == '03':
	hour_colour = 255,0,255 # pink
	htext = 'Three'
elif time_h == '04':
	hour_colour = 0,22,233 # blue
	htext = 'Four'
elif time_h == '05':
	hour_colour = 80,5,112 # yellow
	htext = 'Five'
elif time_h == '06':
	hour_colour = 128,128,0 # olive
	htext = 'Six'
elif time_h == '07':
	hour_colour = 0,255,0 # green
	htext = 'Seven'
elif time_h == '08':
	hour_colour = 0,0,255 # blue
	htext = 'Eight'
elif time_h == '09':
	hour_colour = 255,0,0 # red
	htext = 'Nine'
elif time_h == '10':
	hour_colour = 124,252,0 # pea green
	htext = 'Ten'
elif time_h == '11':
	hour_colour = 0,255,255 # cyan
	htext = 'Eleven'
elif time_h == '12':
	hour_colour = 148,0,211 # purple
	htext = 'Twelve'
else:
	hour_colour = 255,255,255 # white
	htext = 'Error !!!!!!'



	
# Set image picture maps
x = hour_colour
o = [0,0,0]

qpast = [
o,o,o,o,x,o,o,o,
o,o,o,o,x,x,o,o,
o,o,o,o,x,x,x,o,
x,x,x,x,x,x,x,x,
x,x,x,x,x,x,x,x,
o,o,o,o,x,x,x,o,
o,o,o,o,x,x,o,o,
o,o,o,o,x,o,o,o
]

hpast = [
o,o,o,x,x,o,o,o,
o,o,o,x,x,o,o,o,
o,o,o,x,x,o,o,o,
o,o,o,x,x,o,o,o,
x,x,x,x,x,x,x,x,
o,x,x,x,x,x,x,o,
o,o,x,x,x,x,o,o,
o,o,o,x,x,o,o,o
]

qto = [
o,o,o,x,o,o,o,o,
o,o,x,x,o,o,o,o,
o,x,x,x,o,o,o,o,
x,x,x,x,x,x,x,x,
x,x,x,x,x,x,x,x,
o,x,x,x,o,o,o,o,
o,o,x,x,o,o,o,o,
o,o,o,x,o,o,o,o
]

oclock = [
o,o,o,x,x,o,o,o,
o,o,x,x,x,x,o,o,
o,x,x,x,x,x,x,o,
x,x,x,x,x,x,x,x,
o,o,o,x,x,o,o,o,
o,o,o,x,x,o,o,o,
o,o,o,x,x,o,o,o,
o,o,o,x,x,o,o,o
]

off = [
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o,
o,o,o,o,o,o,o,o
]

if time_m == '15':
	qimage = qpast
	qtext = htext + ' Fifteen' + ampm
elif time_m == '30':
	qimage = hpast
	qtext = htext + ' Thirty' + ampm
elif time_m == '45':
	qimage = qto
	qtext = htext + ' Forty Five' + ampm
else:
	qimage = oclock
	qtext = htext + ' o\'Clock' + ampm + time_d
	
	
i1 = 0
while (i1 <= min_flash):
	sense.set_pixels(qimage)
	time.sleep(frame_delay)
	sense.set_pixels(off)
	time.sleep(frame_delay)
	i1 += 1
	
time.sleep(pause_delay)
	
i = 1
while (i <= repeat):
	
	sense.show_message(qtext, scroll_speed=txt_scroll_speed, text_colour=hour_colour, back_colour=[0,0,0])
	time.sleep(pause_delay)
	i += 1
	

i = 1
while (i <= repeat):
	
	sense.show_message(time_flash, scroll_speed=txt_scroll_speed, text_colour=hour_colour, back_colour=[0,0,0])
	time.sleep(pause_delay)
	i += 1

