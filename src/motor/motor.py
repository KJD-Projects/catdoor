from gpiozero import LED
import time


class Motor:

    def __init__(self):
        self.red_led = LED(8)
        self.grn_led = LED(25)


    def found_cat(self):
        for i in range(15):
            self.grn_led.on()
            time.sleep(.1)
            self.grn_led.off()
            time.sleep(.1)
            self.red_led.on()
            time.sleep(.1)
            self.red_led.off()
            time.sleep(.1)

    def found_cup(self):
        for i in range(15):
            self.grn_led.on()
            time.sleep(.1)
            self.grn_led.off()
            time.sleep(.1)
            self.red_led.on()
            time.sleep(.1)
            self.red_led.off()
            time.sleep(.1)
    
    def found_dog(self):
        for i in range(5):
            self.grn_led.on()
            time.sleep(.1)
            self.grn_led.off()
            time.sleep(.1)
            self.red_led.on()
            time.sleep(.1)
            self.red_led.off()
            time.sleep(.1)

    def open_door(self):
        # future feature for servo / stepper motor control
        print("future")
