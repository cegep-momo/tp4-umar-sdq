from controler import controlleur

if __name__ == "__main__":
    control = controlleur.Controlleur()
    try:
        control.demarrage_capteur_distance()
    except KeyboardInterrupt:
        print("Programme arret")