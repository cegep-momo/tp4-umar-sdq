from gpiozero import Button, DistanceSensor
from time import sleep
from datetime import datetime
import json

from model.platine import Platine
from model.moduleTP4 import Mesure
from view.view import View

class Controlleur:

    def __init__(self):
        self.platine = Platine()
        self.view = View()
        self.mesures = []

    def demarrage_capteur_distance(self):
        while True:
            if self.platine.bouton1.is_pressed:
                cm = self.platine.capteur.distance * 100
                temps = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                mesure = Mesure(temps, [round(cm, 2)])
                self.mesures.append(mesure)
                self.view.ecrire_mesure("Distance: " + str(round(cm, 2)) + " cm")
                sleep(1)

            if self.platine.bouton2.is_pressed:
                self.view.ecrire_mesure("Mesure arretee et sauvegardee.")
                self.sauvegarder_mesures()
                sleep(1)
                break

    def sauvegarder_mesures(self):
        data = []
        for m in self.mesures:
            data.append({
                "dateHeureMesure": m.dateHeureMesure,
                "dataMesure": m.dataMesure
            })
        with open("mesures.json", "w") as f:
            json.dump(data, f, indent=4)
