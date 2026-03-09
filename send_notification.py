import network
import urequests as requests
from do_connect import *
from time import sleep
from machine import Pin

#Vincentius Jeremy Tirtawijaya, ENGR 121, Winter 2026
#Send Notification
#March 8th, 2026
#This program's behavior is to send a notification to a phone when pir sensor detects motion

def send_notification():
    '''Parameters (0):
    Functionality: send notification to phone via ntfy app
    Return: None
    '''
    r = requests.post("https://ntfy.sh/MotionDetected",
                     data="Movement detected by sensor",
                     headers={
                         "Title": "ALERT: MOVEMENT DETECTED",
                         "Priority": "5",
                         "Tags": "rotating_light",
                         })
    print("Movement detected, notification sent")
   #Free Raspberry pi memory
    r.close()

pir = Pin(16, Pin.IN, Pin.PULL_UP)


do_connect()

while True:
   if pir.value() == 0:
#        print(pir.value())
       send_notification()
   else:
       pass
   sleep(10)