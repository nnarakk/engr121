import network
import urequests as requests
from do_connect import *
from time import sleep
from machine import Pin


pir = Pin(13, Pin.IN)
led = Pin(14, Pin.OUT)
buzzer = Pin(15, Pin.OUT)

led.off()
buzzer.off()

def send_notification():
    '''
    Parameters: None
    Functionality: Sends a notification to a phone using ntfy
    Return: None
    '''
    r = requests.post(
        "https://ntfy.sh/MotionDetected",
        data="Movement detected by sensor",
        headers={
            "Title": "ALERT: MOVEMENT DETECTED",
            "Priority": "5",
            "Tags": "rotating_light",
        }
    )
    print("Movement detected, notification sent")
    r.close()

do_connect()

notification_sent = False

while True:
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

        
        if not notification_sent:
            send_notification()
            notification_sent = True

    else:
        print("No motion.")
        led.off()
        buzzer.off()
        notification_sent = False

    sleep(1)