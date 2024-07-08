import board
import time
import datetime
import neopixel
import math

# setup the pixels
num_pixels=60
pixels = neopixel.NeoPixel(board.D18, num_pixels, auto_write=False)
bri=255
toff=-26 # 25 if you get spot on 5 oclock entry

def drawPix(pcnt, w, mult):
    sp = (toff + min(num_pixels, round(pcnt*num_pixels))) % num_pixels
    lb = bri
    for i in range(w):
        #print(f"i:{i} lb:{lb}")
        pixels[sp]=(
                    min(255, pixels[sp][0] + lb*mult[0]),
                    min(255, pixels[sp][1] + lb*mult[1]),
                    min(255, pixels[sp][2] + lb*mult[2]),
                    )

        lb = lb*.2
        sp = sp-1
        if sp < 0:
            sp = num_pixels-1

# while forever
while True:
    t = datetime.datetime.now().time()
    s = t.second/60
    m = t.minute/60
    h = (t.hour % 12)/12
    print(f"{t.hour:02d}:{t.minute:02d}:{t.second:02d}")

    pixels.fill((0,0,0))
    drawPix(h, 1, (1,0,0))
    drawPix(m, 1, (0,1,0))
    drawPix(s, 3, (0,0,1))
    pixels.show()
    time.sleep(0.1)
