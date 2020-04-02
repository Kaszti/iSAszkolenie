#Programowanie obiektowe
class Samochod():
    kolory = ('biały', 'czerwony', 'rozowy')
    def __init__(self, kolor_id = 0, marka_parametr = 'BMW'):
        self.abs = None
        self.marka = marka_parametr
        self.kolor = kolory[kolor_id]
        self.cena = '100000 PLN'
samochod_1 = Samochod(0, 'BMW')
print(samochod_1.kolor)
print(samochod_1.marka)
samochod_2 = Samochod(2, 'Fiat')
print(samochod_2.kolor)
print(samochod_2.marka)