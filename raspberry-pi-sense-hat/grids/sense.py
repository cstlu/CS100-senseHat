from sense_hat import SenseHat
import time

from rupee import rupee1, rupee2, rupee3, rupee4

sense = SenseHat()
frame = 1
frames = {
    'rupee1': rupee1,
    'rupee2': rupee2,
    'rupee3': rupee3,
    'rupee4': rupee4,
}

while True:
    sense.set_pixels(frames['rupee' + str(frame)])
    if frame < 4:
        frame += 1
    else:
        frame = 1
    time.sleep(0.3)
