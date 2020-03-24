import moduly.validator as validator
liczba = input('Podaj liczbę')
liczba = liczba.replace(',', '.')
validator.is_number(liczba)