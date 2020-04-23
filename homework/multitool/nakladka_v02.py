from homework import hm_01 as hm
import hm_02_rozmieniarka as rozmieniarka
import hm_02_piramida as pir
import hm_02_pies as pies
import my_modules.hungry_python_isa as hungry_python
import random
import sys
from colorama import Fore

def menu(programs):
    print(Fore.BLUE + 'Witaj w Multitool Python - wersja 2.01')
    for key, program in programs.items():
        print(f'{key} - {program["name"]}')
def another():
    question = input('Czy wykonac inny program (tak/nie)? ')
    if question == 'nie':
        print(Fore.RED + 'Wyszedles z aplikacji.')
        sys.exit(0)
    elif question == 'tak':
        menu(programs)
        choice = input('Twoj wybor: ')
        main(choice)
def leave():
    print(Fore.RED + 'Wyszedles z aplikacji.')
    sys.exit(0)
def random_program():
    r_choice_n = random.randint(1, 13)
    r_choice_S = str(r_choice_n)
    print(f'Wylosowales program o numerze: {r_choice_S}')
    main(r_choice_S)
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
    '14' : {'name': 'Hungry python game', 'function': hungry_python.game_loop},
    'R' : {'name': 'Wyjście z programu', 'function': random_program},
    'X' : {'name': 'Wyjście z programu', 'function': leave},
}
def main(choice):
    try:
        programs[choice]['function']()
        another()
    except KeyError:
        print('Taki program nie isnieje')
        another()
menu(programs)
choice = input('Twoj wybor: ')
main(choice)