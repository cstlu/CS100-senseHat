from sense_hat import SenseHat
import time, sys

sense = SenseHat()
sense.set_rotation(180)


red = [255,0,0]
orange = [255,127,0]
yellow = [255,255,0]
green = [0,255,0]
blue = [0,0,255]
indego = [75,0,130]
violet = [159,0,255]
black = [0,0,0]

x = [0,255,0]
o = [0,0,0]
r = [255,0,0]
frame_delay = 0.2
pause_delay = 2
repeat = 50



image1 = [
o,x,o,o,o,o,x,o,
o,o,x,o,o,x,o,o,
o,o,x,x,x,x,o,o,
o,x,r,x,x,r,x,o,
x,o,x,x,x,x,o,x,
x,o,x,x,x,x,o,x,
o,o,x,o,o,x,o,o,
o,x,o,o,o,o,x,o
]

image2 = [
o,x,o,o,o,o,x,o,
o,o,x,o,o,x,o,o,
x,o,x,x,x,x,o,x,
x,x,r,x,x,r,x,x,
o,o,x,x,x,x,o,o,
o,o,x,x,x,x,o,o,
o,o,x,o,o,x,o,o,
o,o,o,x,x,o,o,o
]

image3 = [
o,o,o,x,x,o,o,o,
o,x,x,x,x,x,x,o,
x,x,x,x,x,x,x,x,
x,r,r,x,x,r,r,x,
x,x,x,x,x,x,x,x,
o,o,x,o,o,x,o,o,
o,x,o,x,x,o,x,o,
x,o,o,o,o,o,o,x
]

image4 = [
o,o,o,x,x,o,o,o,
o,x,x,x,x,x,x,o,
x,x,x,x,x,x,x,x,
x,r,r,x,x,r,r,x,
x,x,x,x,x,x,x,x,
o,x,o,o,o,o,x,o,
x,o,o,x,x,o,o,x,
x,x,x,o,o,x,x,x
]

image5 = [
o,o,o,x,x,o,o,o,
o,o,x,x,x,x,o,o,
o,x,r,x,x,r,x,o,
x,x,x,x,x,x,x,x,
x,x,x,x,x,x,x,x,
o,x,o,x,x,o,x,o,
x,o,o,o,o,o,o,x,
o,x,o,o,o,o,x,o
]

image6 = [
o,o,o,x,x,o,o,o,
o,o,x,x,x,x,o,o,
o,x,r,x,x,r,x,o,
x,x,x,x,x,x,x,x,
x,x,x,x,x,x,x,x,
o,o,x,o,o,x,o,o,
o,x,o,x,x,o,x,o,
x,o,x,o,o,x,o,x
]

image7 = [
o,o,o,x,x,o,o,o,
o,o,x,x,x,x,o,o,
o,x,x,x,x,x,x,o,
x,x,o,x,o,x,o,x,
x,x,x,x,x,x,x,x,
x,x,x,x,x,x,x,x,
o,x,o,x,x,o,x,o,
o,x,o,o,o,o,x,o
]

image8 = [
o,o,o,x,x,o,o,o,
o,o,x,x,x,x,o,o,
o,x,x,x,x,x,x,o,
x,o,x,o,x,o,x,x,
x,x,x,x,x,x,x,x,
x,x,x,x,x,x,x,x,
o,x,o,x,x,o,x,o,
o,x,o,o,o,o,x,o
]



i1 = 1
while (i1 <= repeat):
	sense.set_pixels(image1)
	time.sleep(frame_delay)
	sense.set_pixels(image2)
	time.sleep(frame_delay)
	i1 += 1
	
time.sleep(pause_delay)
	
i2 = 1
while (i2 <= repeat):
	sense.set_pixels(image3)
	time.sleep(frame_delay)
	sense.set_pixels(image4)
	time.sleep(frame_delay)
	i2 += 1
	
time.sleep(pause_delay)
	
i3 = 1
while (i3 <= repeat):
	sense.set_pixels(image5)
	time.sleep(frame_delay)
	sense.set_pixels(image6)
	time.sleep(frame_delay)
	i3 += 1
	
time.sleep(pause_delay)
	
i4 = 1
while (i4 <= repeat):
	sense.set_pixels(image7)
	time.sleep(frame_delay)
	sense.set_pixels(image8)
	time.sleep(frame_delay)
	i4 += 1
	
time.sleep(pause_delay)
	
	
print "Program Complete - System Exiting...."
sense.show_message("Python Programming by CathalStewart.co.uk.........;-)", scroll_speed=0.05, back_colour=[0,0,0])
time.sleep(pause_delay)
sys.exit()
