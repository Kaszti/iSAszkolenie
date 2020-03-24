def licznik():
    try:
        with open('licznik.txt', 'r+') as plik:
            ilosc_uruchomien = plik.read()
            plik.seek(0)
            try:
                ilosc_uruchomien = int(ilosc_uruchomien)
                ilosc_uruchomien +=1
            except:
                ilosc_uruchomien = 1
            plik.write(str(ilosc_uruchomien))
            print(ilosc_uruchomien)
    except FileNotFoundError:
        with open('licznik.txt', 'w') as plik:
            plik.write('1')
            print('1')
licznik()