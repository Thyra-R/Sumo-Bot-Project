import math, time
import machine
from machine import PWM
from machine import Pin

time.sleep(1) # Wait for USB to become ready

pwm_rate = 2000

#Set pins for motor control (1 and 2)
ain1_ph = Pin(12, Pin.OUT)
ain2_en = PWM(13, freq = pwm_rate, duty_u16 = 0)
motCTRL2 = Pin(14, Pin.OUT)
motSPD2 = PWM(15, freq = pwm_rate, duty_u16 = 0)

#Setting pwm
pwm = min(max(int(2**16 * abs(1)), 0), 65535)

while True:
    #Setting motors to drive forward
    print("Motor Forward") # Print to REPL
    ain1_ph.low() #set Motor1 Forward Direction
    ain2_en.duty_u16(pwm) #Motor 1 Speed/Power
    motCTRL2.low() #set Motor 2 Forward Direction
    motSPD2.duty_u16(pwm) #Motor 2 Speed/Power
    time.sleep(2)
    #Turning off motors (setting both motor poweres to 0 pwm)
    print("Motor OFF")
    ain2_en.duty_u16(0)
    motSPD2.duty_u16(0)
    time.sleep(2)
    #Same as 2 blocks above but for reverse
    print("Motor Reverse")
    ain1_ph.high()
    ain2_en.duty_u16(pwm)
    motCTRL2.high()
    motSPD2.duty_u16(pwm)
    time.sleep(2)
    #Turning motors off again
    print("Motor OFF")
    ain1_ph.low()
    ain2_en.duty_u16(0)
    motSPD2.duty_u16(0)
    time.sleep(2)