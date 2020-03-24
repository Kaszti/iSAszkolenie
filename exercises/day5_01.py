# slownik = {}
# slownik['imiona'] = ['Ala', 'Jan']
# slownik.update({'nazwiska': ['Kowal', 'Malina']})
# print(slownik)
# wiersze = [
#     {'imie': 'Adam', 'nazwisko': 'Pałą'},
#     {'imie': 'Daniel', 'nazwisko': 'Jakiś'},
#     {'imie': 'Marta', 'nazwisko': 'Makota'}
# ]
# for klucz, wartosc in slownik.items():
#     print(klucz)
#     print(wartosc)


# do slownika odowlujemy sie jak do listy tylko nie indexem a nazwa!
wiersze = [
    {'imie': 'Łukasz', 'naziwsko': 'Falkowicz'},
    {'imie': 'Adam', 'naziwsko': 'Falkowicz'},
    {'imie': 'Jan', 'naziwsko': 'Falkowicz'},
]
for element in wiersze:
    # print(element)
    print(f"Mam na imię: {element['imie']}")