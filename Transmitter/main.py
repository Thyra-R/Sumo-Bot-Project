import ir_tx
import time
import machine
from ir_tx.nec import NEC
from machine import Pin

tx_pin = Pin(18, Pin.OUT, value=0)
device_addr = 0x01
transmitter = NEC(tx_pin)
commands = [0x01,0x02,0x03,0x04,0x05]

LED = Pin(15, Pin.OUT)

if __name__ == "__main__":
    while True:
        for command in commands:
            transmitter.transmit(device_addr,command)
            print("COMMANDS",hex(command),"TRANSMITTED.")
            LED.value(1)
            time.sleep(3)

while True:
    LED.value(0)
