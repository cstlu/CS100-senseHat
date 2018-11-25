from sense_hat import SenseHat
import time

from majoras_mask import *

sense = SenseHat()
frames = {
    'frame1':frame1,
'frame2':frame2,
'frame3':frame3,
'frame4':frame4,
'frame5':frame5,
'frame6':frame6,
'frame7':frame7,
'frame8':frame8,
'frame9':frame9,
'frame10':frame10,
'frame11':frame11,
'frame12':frame12,
'frame13':frame13,
'frame14':frame14,
'frame15':frame15,
'frame16':frame16,
'frame17':frame17,
'frame18':frame18,
'frame19':frame19,
'frame20':frame20,
'frame21':frame21,
'frame22':frame22,
'frame23':frame23,
'frame24':frame24,
'frame25':frame25,
'frame26':frame26,
'frame27':frame27,
'frame28':frame28,
'frame29':frame29,
'frame30':frame30,
'frame31':frame31,
'frame32':frame32,
'frame33':frame33,
'frame34':frame34,
'frame35':frame35,
'frame36':frame36,
'frame37':frame37,
'frame38':frame38,
'frame39':frame39,
'frame40':frame40,
'frame41':frame41,
'frame42':frame42
}
framecout = 1
while True:
    sense.set_pixels(frames['frame' + str(framecout)])
    if framecout < 42:
        framecout += 1
    else:
        framecout = 1
    time.sleep(0.1)
