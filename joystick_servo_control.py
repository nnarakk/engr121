import machine
import utime

#Vincentius Jeremy Tirtawijaya, ENGR 121, Winter 2026
#Joystick Servo Control
#March 14th, 2026
#This program's behavior is to control the mount with a joystick

#Y level Servo
servoY = machine.PWM(machine.Pin(18))
#X level Servo
servoX = machine.PWM(machine.Pin(17))
servoY.freq(50)
servoX.freq(50)

x_joystick = machine.ADC(27)
y_joystick = machine.ADC(26)
z_switch = machine.Pin(24,machine.Pin.IN)

def interval_mapping(x, in_min, in_max, out_min, out_max):
    '''Parameters (4):
    x (int): Value read
    in_min (int): Minimum value in
    in_max (int): Max value in
    out_min (int): Min value out
    out_max (int): Max value out
    Functionality: Min-Max Scales data
    Return: int
    '''
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def servo_write(pin,angle):
    '''Parameters (2):
    pin (PWM): Pin connected to servo
    angle (int): Angle of servo
    Functionality: Adjusts servo angle
    Return: None
    '''
    pulse_width=interval_mapping(angle, 0, 180, 0.5,2.5)
    duty=int(interval_mapping(pulse_width, 0, 20, 0,65535))
    pin.duty_u16(duty)

x_angle = 0
y_angle = 0

while True:    
    x_value = x_joystick.read_u16()
    y_value = y_joystick.read_u16()
    z_value = z_switch.value()
#     print(x_value,y_value,z_value)
    
    if y_angle >= 0 and y_angle <= 180:
        if y_value >= 32000 and y_value <= 34000:
            y_angle += 0
        elif y_value < 32000 and y_angle != 0:
             y_angle -= 1
        elif y_value > 34000 and y_angle != 180:
             y_angle += 1
             
    if x_angle >= 0 and x_angle <= 180:
        if x_value >= 32000 and x_value <= 34000:
            x_angle += 0
        elif x_value < 32000 and x_angle != 0:
             x_angle -= 1
        elif x_value > 34000 and x_angle != 180:
             x_angle += 1
             
        
#     print(x_angle)
#     print(y_angle)
    utime.sleep_ms(10)
    
    servo_write(servoX,x_angle)
    servo_write(servoY,y_angle)
    