import unittest
from gpiozero import Device
from gpiozero.pins.mock import MockFactory
from model.platine import Platine

Device.pin_factory = MockFactory()

class TestPlatine(unittest.TestCase):
    def setUp(self):
        self.platine = Platine(gpio_btn1=16, gpio_btn2=21)

    def test_bouton1_presse(self):
        self.platine.bouton1.pin.drive_low()
        self.assertTrue(self.platine.bouton1.is_active)

    def test_bouton2_presse(self):
        self.platine.bouton2.pin.drive_low()
        self.assertTrue(self.platine.bouton2.is_active)

   

if __name__ == "__main__":
    unittest.main()
