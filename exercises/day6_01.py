plik = open('test.txt', 'rb+')
print(plik.tell()) #pokazuje gdzie kursor jest
print(plik.readline(), end='') #czyta linijke
print(plik.tell())
print(plik.seek(-5, 2)) #ustawianie kursora
print(plik.seek(0))
wszystkie_linie = plik.readlines()
print(wszystkie_linie)
print(plik.readline(), end='')
plik.close()


with open('test.txt', 'r+') as plik:
    print(plik.tell())  # pokazuje gdzie kursor jest
    wszystkie_linie = plik.readlines()
    print(wszystkie_linie)
    print(plik.tell())
    try:
        plik.writelines(['\n1', '\n2'])
    except:
        print('Nie masz uprawnien do zapisu')
    print(plik.tell())