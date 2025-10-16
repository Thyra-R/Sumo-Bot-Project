import machine, time
from machine import Pin

Red = Pin(12, Pin.OUT)
Blue = Pin(13, Pin.OUT)
Green = Pin(14, Pin.OUT)

while True:
    Red.value(1)
    Blue.value(1)
    Green.value(1)
    print("On")
    time.sleep(1)
    Red.value(0)
    Blue.value(0)
    Green.value(0)
    print("Off")
    time.sleep(1)