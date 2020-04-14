#pseudo prywatne pola i metody

from __future__ import annotations
import pprint

class Ksiazka():
    stawka_vat = 23  #pole klasy

    __marza = 10

    def __init__(self, autor, tytul, ilosc_stron):
        self.autor = autor
        self.tytul: str = tytul
        self.ilosc_stron = ilosc_stron
        self.__ocena = 1

    def podaj_tytul(self):
        return f'{self.tytul.capitalize()} z oceną: {self.__ocena} oraz marza: {self.__jaka_marza()}'
    def __jaka_marza(self):
        return self.__marza

    @classmethod  #metody klasy
    def pan_tadeusz(cls):
        """
        Docstring tej metody
        :return: tworzy pana tadeusza
        """
        print(cls.__marza)
        return cls('Adam Mickiewicz', 'Pan Tadeusz', 500)


    @classmethod
    def jaki_vat(cls):
        return f'{cls.stawka_vat}% VAT'

    @staticmethod
    def ktora_grubsza(param_1: Ksiazka, param_2: Ksiazka) -> str:
        if param_1.ilosc_stron > param_2.ilosc_stron:
            return 'Pierwsza jest grubsza'
        else:
            return 'Druga jest grubsza'
    @staticmethod
    def czy_promocja():
        pass
        #if swiatowy dzien ksiazki == now():
        #print('Promocja')
# print(Ksiazka.jaki_vat())
# ksiazka_1 = Ksiazka('Sienku', 'potop', 300)
# print(ksiazka_1.podaj_tytul())
# ksiazka_2 = Ksiazka.pan_tadeusz()
# print(ksiazka_2.podaj_tytul())
# print(Ksiazka.ktora_grubsza(ksiazka_1, ksiazka_2))

# print(Ksiazka.pan_tadeusz())
# ksiazka = Ksiazka.pan_tadeusz()
# print(ksiazka.podaj_tytul())
# print(Ksiazka.__marza) nie zadziala bo jest pseudoprywatne
pprint.pprint(Ksiazka.__dict__)