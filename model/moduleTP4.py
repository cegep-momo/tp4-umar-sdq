class Mesure:

    def __init__(self, dateHeureMesure, dataMesure):
        self.dateHeureMesure = dateHeureMesure
        self.dataMesure = dataMesure
    def __repr__(self):
        return {self.dateHeureMesure}, {self.dataMesure}
    
    def afficherMesure(self):
        print(f"Temps de mesure: {self.dateHeureMesure}")
        print(f"Mesure: {self.dataMesure}")