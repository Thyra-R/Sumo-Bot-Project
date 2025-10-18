import math, time

#import ir_rx
import machine
from machine import PWM
from machine import Pin
#from ir_rx.nec import NEC_8 # Use the NEC 8-bit class
#from ir_rx.print_error import print_error # for debugging

time.sleep(1) # Wait for USB to become ready

pwm_rate = 2000

#Set pins for motor control (1 and 2)
ain1_ph = Pin(12, Pin.OUT)
ain2_en = PWM(13, freq = pwm_rate, duty_u16 = 0)
motCTRL2 = Pin(14, Pin.OUT)
motSPD2 = PWM(15, freq = pwm_rate, duty_u16 = 0)

#Setting pwm
pwm = min(max(int(2**16 * abs(1)), 0), 65535)

#Interrupt
def ir_callback(data, addr, _):
    print(f"Received NEC command! Data: 0x{data:02X}, Addr: 0x{addr:02X}")

# Setup the IR receiver
#ir_pin = Pin(17, Pin.IN, Pin.PULL_UP) # Adjust the
#ir_receiver = NEC_8(ir_pin, callback=ir_callback)

#ir_receiver.error_function(print_error)

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