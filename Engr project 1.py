#Tyssen Chiu, ENGR 121, Winter 2026
#Servo and camera
#March 8th, 2036
#This program's behavior is to make the servo rotate when the camera detects a large object
from gpiozero import AngularServo
from time import sleep
import cv2
import numpy as np

servo = AngularServo(18)
servo.angle = 0


# Sets up the camera and the resolution.
picam2 = Picamera2()
config = picam2.create_preview_configuration(main={"size": (640, 480)})
picam2.configure(config)
picam2.start()

sleep(2)


# takes a picture so it can compare to the others later to detect motion
previous_frame = picam2.capture_array()

angle = 0
# keeps track of the servo angle

# It will keep checking if something moved
while True:

    frame = picam2.capture_array()
    # take a new picture from the camera


    # Convert the image to grey so the code can see what changed between frames
    gray1 = cv2.cvtColor(previous_frame, cv2.COLOR_RGB2GRAY)
    gray2 = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    difference = cv2.absdiff(gray1, gray2)

    thresh = cv2.threshold(difference, 25, 255, cv2.THRESH_BINARY)[1]


    # looks for the biggest object
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    biggest_contour = None
    biggest_area = 0

    for contour in contours:
        area = cv2.contourArea(contour)

        if area > biggest_area:
            biggest_area = area
            biggest_contour = contour


    # If a moving object is detected it will find the center of the object and it will move left to right
    if biggest_contour is not None and biggest_area > 1000:

        x, y, w, h = cv2.boundingRect(biggest_contour)

        center_x = x + w // 2

        if center_x < 270:
            angle -= 5

        elif center_x > 370:
            angle += 5


        # servo does not rotate super far
        if angle < -90:
            angle = -90

        if angle > 90:
            angle = 90

        servo.angle = angle

        print("Tracking object at angle:", angle)

    # The current frame becomes the previous frame so it can do the loop again
    previous_frame = frame

    sleep(0.1)


