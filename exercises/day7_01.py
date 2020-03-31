#debugger i evaluate expression
tydzien = ['pon', 'wt', 'śr', 'czw', 'pia', 'sob', 'nie']
weekend = ['sob', 'nie']
lista = [
    {
        'imie': 'Łukasz',
        'adresy': ['Adres 1','Adres 2'],
        'telefony': {'dom': '43524545', 'praca': '+48 56456546'}
    }
]
print(lista[0]['telefony']['praca'])
def wyswietl(text):
    print(text)
for dzien in tydzien:
    if dzien in weekend:
        wyswietl('Jest Weekend!')