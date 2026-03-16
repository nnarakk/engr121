# import network
# import urequests as requests
# from do_connect import *
from time import sleep
from machine import Pin
from send_notification import *
from joystick_servo_control import *


pir = Pin(14, Pin.IN)
led = Pin(16, Pin.OUT)
buzzer = Pin(15, Pin.OUT)

led.off()
buzzer.off()

#Y level Servo
servoY = machine.PWM(machine.Pin(18))
#X level Servo
servoX = machine.PWM(machine.Pin(17))
servoY.freq(50)
servoX.freq(50)

x_joystick = machine.ADC(27)
y_joystick = machine.ADC(26)
z_switch = machine.Pin(24,machine.Pin.IN)

x_angle = 0
y_angle = 0

# do_connect()

while True:
    x_angle, y_angle = joystick_control(x_angle,y_angle)
    servo_write(servoX,x_angle)
    servo_write(servoY,y_angle)
    utime.sleep_ms(10)
        
    motion = pir.value()
 
    if motion == 1:
        print("Motion detected!")
         
        for i in range(10):
            led.on()
            buzzer.on()
            sleep(0.2)
            led.off()
            buzzer.off()
            sleep(0.2)

        send_notification()

    else:
        print("No motion.")
        led.off()
        buzzer.off()