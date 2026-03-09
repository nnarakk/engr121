import machine
import utime

pir = machine.Pin(13, machine.Pin.IN)
led = machine.Pin(14, machine.Pin.OUT)
buzzer = machine.Pin(15, machine.Pin.OUT)

led.off()
buzzer.off()

def motion_detected(pin):
    while True:
        motion = pir.value()
        if motion == 1:
            for i in range (10):
                print("Motion detected!")
                led.on()
                buzzer.on()
                utime.sleep(0.2)
                led.off()
                buzzer.off()
                utime.sleep(0.2)
        else:
            print("No motion.")
            led.off()
            buzzer.off()

pir.irq(trigger=machine.Pin.IRQ_RISING, handler=motion_detected)