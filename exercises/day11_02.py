#pola klasy

class Ksiazka():
    stawka_vat = 23  #pole klasy
    def __init__(self, autor, tytul):
        self.autor = autor
        self.tytul = tytul
print(Ksiazka.stawka_vat)
ksiazka = Ksiazka('Sienku', 'Potop')
print(Ksiazka)