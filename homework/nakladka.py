import hm_01 as hm
import hm_02_rozmieniarka as rozmieniarka
import hm_02_piramida as pir
import hm_02_pies as pies
import random
import sys
from colorama import Fore

def another():
    question = input('Czy wykonac inny program (tak/nie)? ')
    if question == 'nie':
        print(Fore.RED + 'Wyszedles z aplikacji.')
        sys.exit(0)
    elif question == 'tak':
        intro()
        choice = input('Twoj wybor: ')
        main(choice)
def main(choice):
    if choice == '1':
        hm.cf()
        another()
    elif choice == '2':
        hm.fc()
        another()
    elif choice == '3':
        hm.pk()
        another()
    elif choice == '4':
        hm.pioc()
        another()
    elif choice == '5':
        hm.prostokat()
        another()
    elif choice == '6':
        hm.bd()
        another()
    elif choice == '7':
        hm.parity()
        another()
    elif choice == '8':
        hm.p357()
        another()
    elif choice == '9':
        hm.p3i5i7()
        another()
    elif choice == '10':
        hm.yearp()
        another()
    elif choice == '11':
        rozmieniarka.changer()
        another()
    elif choice == '12':
        pir.piramida()
        another()
    elif choice == '13':
        pies.age_d()
        another()
    elif choice == 'R' or choice == 'r':
        r_choice_n = random.randint(1, 13)
        r_choice_S = str(r_choice_n)
        print(f'Wylosowales program o numerze: {r_choice_S}')
        main(r_choice_S)
        another()
    elif choice == 'X' or choice == 'x':
        print(Fore.RED + 'Wyszedles z aplikacji.')
        sys.exit(0)
    else:
        error()
def intro():
    print(Fore.WHITE + '''Wybierz program ktory chcesz uruchomic
1) Przeliczanie C -> F
2) Przeliczanie F -> C
3) Obliczanie pola powierzchni kola
4) Sprawdzanie pierwszej i ostatniej cyfry
5) Rysowanie prostokata
6) Przeliczanie liczby zapisanej w formacie binarnym na dziesietny
7) Rozpoznawanie parzystosci
8) Podzielnosc przez 3 lub 5 lub 7
9) Podzielnosc przez 3 i 5 i 7
10) Sprawdzanie przestępczości roku
11) Rozmieniarka
12) Rysowanie piramidy
13) Kalkulator wieku psa
R) Wybierz program losowo
X) Wyjście z programu''')
def error():
    print('Podano bledny wybor. Wybierz poprawna opcje z listy.')
    intro()
    choice = input('Twoj wybor: ')
    main(choice)
print(Fore.BLUE + 'Witaj w Multitool Python Program by iSA - wersja B02.12321')
intro()
choice = input('Twoj wybor: ')
main(choice)