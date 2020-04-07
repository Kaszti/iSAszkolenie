class Ksiazka():
    def __init__(self, tytul, autor, cena=19.99, vat = 7, ilosc_stron=100):
        self.tytul = tytul
        self.ilosc_stron = ilosc_stron
        self.autor = autor
        self.cena_brutto = cena
        self.cena_netto = round(cena / ((100 + vat)/100), 2)
        self.vat = vat

    def __str__(self):
        return f'Tytul: {self.tytul}, autor: {self.autor}'

    def __len__(self):
        return self.ilosc_stron

    # def __add__(self, other):
    #     if isinstance(other, Ksiazka):
    #         return self.ilosc_stron + other.ilosc_stron
    #     else:
    #         print('Tak naprawde nie dodalem nic')
    #         return self.ilosc_stron


class Ebook(Ksiazka):
    def __init__(self, tytul, autor, cena, vat = 23):
        super().__init__(tytul, autor, cena, vat)
        self.format = 'pdf'


class Koszyk():
    def __init__(self):
        self.obiekty = []
        self.ilosc_obiektow = 0
        self.netto = 0
        self.brutto = 0


    def dodaj(self, obiekt):
        self.obiekty.append(obiekt)
        self.ilosc_obiektow += 1
        self.netto += obiekt.cena_netto
        self.brutto += obiekt.cena_brutto

    def __len__(self):
        return len(self.obiekty)

# ksiazka = Ksiazka('Potop', 'Sienkiewicz', 1000)
# ksiazka2 = Ksiazka('Trylogia', 'Sienkiewicz', 3000)
#
# ebook_1 = Ebook('Potop', 'Sienkiewicz')
# print(ebook_1)
# # # print(ksiazka)
# # # print(len(ksiazka))
# # string = 'Ala ma kocura'
# # wynik = ksiazka + string
# # print(wynik)
# # wynik = ksiazka + ksiazka2
# # print(wynik)
# #
# #
# # # class Rodzic():
# # #     pass
# # #
# # # class Dziecko(Rodzic):
# # #     pass

ksiazka_1 = Ksiazka('Potop', 'Sienkiewicz', 25)
ksiazka_2 = Ksiazka('Trylogia', 'Sienkiewicz', 40)
ebook_1 = Ebook('Potop', 'Sienkiewicz', 20)
koszyk = Koszyk()
koszyk.dodaj(ebook_1)
koszyk.dodaj(ksiazka_1)
koszyk.dodaj(ksiazka_2)
print(f'Ilosc elementow w koszyku: {len(koszyk)}')
print(f'Wartosc netto koszyka: {koszyk.netto}')
print(f'Wartosc brutto koszyka: {koszyk.brutto}')