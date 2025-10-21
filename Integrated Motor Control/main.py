import math, time

import ir_rx
import machine
from machine import PWM
from machine import Pin
from ir_rx.nec import NEC_8 # Use the NEC 8-bit class
from ir_rx.print_error import print_error # for debugging

Data = 0X00

time.sleep(1) # Wait for USB to become ready

pwm_rate = 2000

def forward():#Setting motors to drive forward
    print("Both motors Forward") # Print to REPL
    Rphase.low() #set Motor1 Forward Direction
    Renable.duty_u16(pwm) #Motor 1 Speed/Power
    Lphase.low() #set Motor 2 Forward Direction
    Lenable.duty_u16(pwm) #Motor 2 Speed/Power

def back(): #Setting motors to drive backwards
    time.sleep(2)
    print("Both motors Reverse")
    Rphase.high()
    Renable.duty_u16(pwm)
    Lphase.high()
    Lenable.duty_u16(pwm)

def left(): #turn the robot left
    time.sleep(2)
    print("Right motor forward, left motor back") #Self explanatory
    Rphase.low()
    Renable.duty_u16(pwm)
    Lphase.high()
    Lenable.duty_u16(1000)

def right(): #turn the robot right
    time.sleep(2)    
    print("Left motor forward, right motor Back") #Self explanatory
    Rphase.high()
    Renable.duty_u16(1000)
    Lphase.low()
    Lenable.duty_u16(pwm)

def stop(): #Turning off motors (setting both motor poweres to 0 pwm)
    time.sleep(2)
    print("Both motors OFF")
    Renable.duty_u16(0)
    Lenable.duty_u16(0)

#Set pins for motor control (1 and 2)
Rphase = Pin(12, Pin.OUT)
Renable = PWM(13, freq = pwm_rate, duty_u16 = 0)
Lphase = Pin(14, Pin.OUT)
Lenable = PWM(15, freq = pwm_rate, duty_u16 = 0)

#Setting pwm
pwm = min(max(int(2**16 * abs(1)), 0), 65535)

#Interrupt Handles transmitter data and calls appropriate function
def ir_callback(data, addr, _):
    print(f"Received NEC command! Data: 0x{data:02X}, Addr: 0x{addr:02X}")#debug
    if(data == 0X01):
        forward()
    elif(data == 0x02):
        back()
    elif(data == 0x03):
        left()
    elif(data == 0x04):
        right()
    else:
        stop()
   
# Setup the IR receiver

ir_pin = Pin(17, Pin.IN, Pin.PULL_UP) # Adjust the
ir_receiver = NEC_8(ir_pin, callback=ir_callback)

ir_receiver.error_function(print_error)

while True:
    pass