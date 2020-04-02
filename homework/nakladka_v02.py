import hm_01 as hm
import hm_02_rozmieniarka as rozmieniarka
import hm_02_piramida as pir
import hm_02_pies as pies
import random
import sys
from colorama import Fore

def menu(programs):
    print(Fore.BLUE + 'Witaj w Multitool Python - wersja 2.01')
    for key, program in programs.items():
        print(f'{key} - {program["name"]}')

    return input('Który program uruchomić? ').upper()

programs = {
    '1' : {'name': 'Przeliczanie C -> F', 'function': hm.cf},
    '2' : {'name': 'Przeliczanie F -> C', 'function': hm.fc},
    '3' : {'name': 'Obliczanie pola powierzchni kola', 'function': hm.pk},
    '4' : {'name': 'Sprawdzanie pierwszej i ostatniej cyfry', 'function': hm.pioc},
    '5' : {'name': 'Rysowanie prostokata', 'function': hm.prostokat},
    '6' : {'name': 'Przeliczanie liczby zapisanej w formacie binarnym na dziesietny', 'function': hm.bd},
    '7' : {'name': 'Rozpoznawanie parzystosci', 'function': hm.parity},
    '8' : {'name': 'Podzielnosc przez 3 lub 5 lub 7', 'function': hm.p357},
    '9' : {'name': 'Podzielnosc przez 3 i 5 i 7', 'function': hm.p3i5i7},
    '10' : {'name': 'Sprawdzanie przestępczości roku', 'function': hm.yearp},
    '11' : {'name': 'Rozmieniarka', 'function': rozmieniarka.changer},
    '12' : {'name': 'Rysowanie piramidy', 'function': pir.piramida},
    '13' : {'name': 'Kalkulator wieku psa', 'function': pies.age_d},
    'R' : {'name': 'Wyjście z programu', 'function': wyjscie},
    'X' : {'name': 'Wyjście z programu', 'function': wyjscie},
}
wybor = None

while wybor != 'X':
    wybor = menu(programy)

    try:
        print('=' * 20)
        programy[wybor]['function']()
        print('=' * 20)
    except KeyError:
        print('Taki program nie isnieje')