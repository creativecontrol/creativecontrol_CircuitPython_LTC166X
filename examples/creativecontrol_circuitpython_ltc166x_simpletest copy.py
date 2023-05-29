# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2023 Thadeus Frazier-Reed for creativecontrol
#
# SPDX-License-Identifier: Unlicense

import random
import time

import board
import busio
import digitalio

DATA_BITS = 12
BIT_DEPTH = 8

cs = digitalio.DigitalInOut(board.GP1)
cs.direction = digitalio.Direction.OUTPUT
cs.value = True

sck = board.GP2
mosi = board.GP3

spi = busio.SPI(sck, MOSI=mosi)

while True:
    value = random.randint(0, 255)
    
    while not spi.try_lock():
        pass

    try:
        spi.configure(baudrate=5000000, phase=0, polarity=0)
        out = 0x0000
        # Set the top 4 bits to the address based on array position.
        out |= 1 << DATA_BITS
        # Set the next n bits based on bit depth.
        out |= value << (DATA_BITS - BIT_DEPTH)
        out_bytes = out.to_bytes(2, 'big')
        print(f'attempting value: {value} {out_bytes} {len(out_bytes)}')
        cs.value = False
        spi.write(out_bytes)
        cs.value = True
    finally:
        spi.unlock()
    
    time.sleep(3)
