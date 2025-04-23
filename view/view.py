from time import sleep
from view import LCD1602

LCD1602.init(0x27,1)

class View:
    def ecrire_mesure(self, message):
        LCD1602.clear()
        debut_message = message[:16]
        fin_message = message[16:32]
        LCD1602.write(0,0, debut_message)
        LCD1602.write(0,1, fin_message)
        sleep(0.1)
        