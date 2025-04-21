import LCD1602
from gpiozero import Button, LED, DistanceSensor
from threading import Thread
from time import sleep
from random import shuffle

class Platine:
    def __init__(self):
        LCD1602.init(0x27, 1)
        self.bouton1 = Button(17)
        self.bouton2 = Button(27)
        self.capteur = DistanceSensor(echo=12, trigger=17, max_distance=3)

    def set_controlleur(self, controlleur):
        self.controlleur = controlleur