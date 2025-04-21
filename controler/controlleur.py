from gpiozero import Button, LED, DistanceSensor
from time import sleep
from view import platine

class Controlleur:

    def __init__(self):
        self.platine = platine.Platine()
        self.capteur = self.platine.capteur
        self.bouton1 = self.platine.bouton1
        self.bouton2 = self.platine.bouton2

    def demarrage_capteur_distance(self):
        while self.bouton1.is_pressed:
            cm = self.capteur.distance * 100
            print("Distance: " + str(cm) + " cm")
            sleep(1)
            