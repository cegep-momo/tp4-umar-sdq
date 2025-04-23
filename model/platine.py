from gpiozero import Button, LED, DistanceSensor
from threading import Thread
from time import sleep
from random import shuffle

class Platine:
    def __init__(self, gpio_btn1=16, gpio_btn2=21, echo=12, trigger=17):
        self.bouton1 = Button(gpio_btn1)
        self.bouton2 = Button(gpio_btn2)
        self.capteur = DistanceSensor(echo=echo, trigger=trigger, max_distance=3)

  