import sys
import hm_01 as hm
def another():
    question = input('Czy wykonac inny program (tak/nie)? ')
    if question == 'nie':
            sys.exit('Wyszedles z aplikacji.')
    elif question == 'tak':
        main()
def main():
    print('Witaj w Multitool Python Program by iSA - wersja B02.12321')
    print('''Wybierz program ktory chcesz uruchomic
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
    choice = input('Twoj wybor: ')
    if choice == '1':
        hm.cf()
        another()
    elif choice == '2':

main()