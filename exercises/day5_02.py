#try-except

try:
    lista = []
    lista[10]
    wynik = zmienna_ktorej_niema
    wynik = 15/0
    print(wynik)
except ZeroDivisionError:
    print('Wystąpił błąd')
except NameError:
    print('Brak zmiennej')
except:
    print('Nie wiem co sie odjaniepawlilo')
# else:
#     print('Bez bledu')
# finally:
#     print('ZAWSZEEEE')