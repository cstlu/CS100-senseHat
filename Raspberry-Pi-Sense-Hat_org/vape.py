from sense_hat import SenseHat

import time, os, sys

sense = SenseHat()
sense.clear()
sense.set_rotation(180)

delay = 0.5
humid_level = 40.5000




humidity = sense.get_humidity()
while True:
    humidity = sense.get_humidity()
    humidity = round(humidity, 4)
    if humidity > humid_level:
		sense.show_message("Too Much Vape !!!", scroll_speed=0.05, text_colour=[255,0,0], back_colour=[0,0,0])
    time.sleep(delay)
    print(humidity)
