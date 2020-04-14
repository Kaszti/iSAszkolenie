#typowanie, hinting i docstring

from typing import List, Dict

def witaj(imie: str, nazwisko: str) -> List:
    """
    Funkcja wita sie z uzytkownikiem
    :param str imie: opis patametru
    :param str nazwisko: opis patametru
    :return: Funkcja zwraca liste imie, nazwisko
    """
    imie = imie.capitalize()
    nazwisko = nazwisko.capitalize()
    print(f'Witaj {imie} {nazwisko}')
    return [imie, nazwisko]
wynik = witaj('adam', 'adamowski')
print(witaj.__doc__)