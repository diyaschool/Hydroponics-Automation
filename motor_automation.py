import RPi.GPIO as GPIO
import time
import smbus
import time
from lcd import *


GPIO.setmode(GPIO.BCM)
motor_pin = 17

GPIO.setup(motor_pin, GPIO.OUT)

def control_motor(duration, state):
    GPIO.output(motor_pin, state)
    time.sleep(duration)


def wait_for(seconds):
    timestamp = time.time() + seconds
    while time.time() < timestamp:
        pass

if __name__ == "__main__":
    try:
        lcd_init()
        while True:
            lcd_string(f"PH Level:5.7", LCD_LINE_2)
            lcd_string("EC Level:1.6", LCD_LINE_3)
            duration_on=10
            duration_off=1
            GPIO.output(motor_pin, GPIO.HIGH)
            lcd_string(f"Motor on for {duration_on}s", LCD_LINE_1)
            wait_for(duration_on)
            
            GPIO.output(motor_pin, GPIO.LOW)
            lcd_string(f"Motor off for {duration_off}s", LCD_LINE_1)
            wait_for(duration_off)
            
       
    except KeyboardInterrupt:
        GPIO.cleanup()


    finally:
        lcd_byte(0x01, LCD_CMD)  
        lcd_string("Motor automation OFF", LCD_LINE_1)




