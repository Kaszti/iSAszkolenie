# Przeliczanie Celsjusza na Fahrenheita
def cf():
    try:
        tc = input('Podaj temperaturę w stopniach celsjusza: ')
        tf = (9 / 5) * float(tc) + 32
        print('TF = (9/5)*TC+32')
        print('Temperatura w stopniach Fahrenheita jest równa: ' + str(tf))
    except:
        print('Podaj liczbę.')
        cf()


#Stopnie Fahrenheita na Celsjusza
def fc():
    try:
        tf = input('Podaj temperaturę w stopniach Fahrenheita: ')
        tc = (5 / 9) * float(tf) - (160 / 9)
        print('TC = (5/9)*TF-(160/9)')
        print('Temperatura w stopniach Celsjusza jest równa: ' + str(tc))
    except:
        print('Podaj liczbe.')
        fc()

#Obliczanie pola powierzchni koła
def pk():
    try:
        r = input('Podaj promień koła w milimetrach: ')
        print('P = pi*(R**2)')
        p = 3.14 * (float(r) ** 2)
        print('Pole powierzchni koła wynosi: ' + str(p) + ' [mm]')
    except:
        print('Podaj liczbe')
        pk()


#Pierwsza i ostatnia cyfra
def pioc():
    try:
        number = input("Podaj dowolną liczbę: ")
        number_check = float(number)
        if number[0] == '-':
            print('Pierwsza cyfra to: ' + str(number[1]) + ', a ostatnia cyfra to: ' + str(number[-1]))
        else:
            print('Pierwsza cyfra to: ' + str(number[0]) + ', a ostatnia cyfra to: ' + str(number[-1]))
    except:
        print('Podaj liczbe.')
        pioc()

#Rysowanie prostokąta
#Z racji tego, że operujemy na liczbach całkowitych ze względu na rysowanie prostokąta za pomocą znaków
#proszę o podanie długości podstawy i boku jako liczby całkowitej, inaczej wyskoczy bład.
#Niestety miałem masę pracy w weekend więc nie bawiłem, się w robienie warunków i program nie wyświetli
#komunikatu, że wpisano złą wartość.
def prostokat():
    try:
        l_base = input('Podaj długość podstawy: ')
        l_side = input('Podaj długość boku: ')
        l_base_w = int(l_base) - 2
        l_side_w = int(l_side) - 2
        print('+' + l_base_w * '-' + '+')
        for user in range(0, l_side_w):
            print('|' + l_base_w * ' ' + '|')
        print('+' + l_base_w * '-' + '+')
    except:
        print('Podaj liczbe calkowita.')
        prostokat()


#przeliczanie liczby zapisanej w formacie binarnym na dziesiętny
def bd():
    try:
        length_check = True
        number_b = input('Podaj liczbę zapisaną w formacie binarnym (6 znaków, tylko 0 lub 1): ')
        if len(number_b) != 6:
            print('Miało być 6 znaków')
            length_check = False
        for i in range(0, len(number_b)):
            if int(number_b[i]) != 0 and int(number_b[i]) != 1:
                print('System binarny zawiera tylko 0 i 1')
                length_check = False
        if length_check == True:
            number_d = int(number_b[0]) * 32 + int(number_b[1]) * 16 + int(number_b[2]) * 8 + int(
                number_b[3]) * 4 + int(
                number_b[4]) * 2 + int(number_b[5]) * 1
            print('Liczba w zapisie binarnym: ' + number_b)
            print('Liczba w zapisie dziesiętnym: ' + str(number_d))
    except:
        print('Liczba binarna zawiera tylko 0 i 1 oraz ma miec dlugosc 6 znakow.')
        bd()


#Rozpoznawanie parzystości
def parity():
    try:
        number = input('Podaj liczbę całkowitą: ')
        parity_check = int(number) % 2
        if parity_check == 0:
            print('Podana liczba jest parzysta! :D')
        else:
            print('Podana liczba jest nieparzysta! :(')
    except:
        print('Miala byc liczba calkowita.')
        parity()



#Podzielność przez 3 lub 5 lub 7
def p357():
    try:
        number = input('Podaj liczbę całkowitą: ')
        divisibility_3 = int(number) % 3
        if divisibility_3 == 0:
            print('Podana liczba jest podzielna przez 3.')
        else:
            print('Podana liczba nie jest podzielna przez 3')
        divisibility_5 = int(number) % 5
        if divisibility_5 == 0:
            print('Podana liczba jest podzielna przez 5.')
        else:
            print('Podana liczba nie jest podzielna przez 5')
        divisibility_7 = int(number) % 7
        if divisibility_7 == 0:
            print('Podana liczba jest podzielna przez 7.')
        else:
            print('Podana liczba nie jest podzielna przez 7')
    except:
        print('Podaj liczbe calkowita.')
        p357()

#Podzielność przez 3 i 5 i 7
def p3i5i7():
    try:
        number = input('Podaj liczbę całkowitą: ')
        dividend = 3 * 5 * 7
        divisibility = int(number) % dividend
        if divisibility == 0:
            print('Liczba jest podzielna przez 3 i 5 i 7.')
        else:
            print('Liczba nie jest podzielna przez 3 i 5 i 7.')
    except:
        print('Podaj liczbe calkowita.')
        p3i5i7()


#Sprawdzanie przestępczości roku (taka gra słów :D)
def yearp():
    try:
        year = input('Podaj rok jaki chciałbyś/chciałabyś sprawdzić.')
        divisibility_4 = int(year) % 4
        divisibility_100 = int(year) % 100
        divisibility_400 = int(year) % 400
        if divisibility_4 == 0 and divisibility_100 != 0:
            print('Podany rok jest przestępny.')
        elif divisibility_400 == 0:
            print('Podany rok jest przestępny.')
        else:
            print('Podany rok nie jest przestępny.')
    except:
        print('Rok jest liczba calkowita.')
        yearp()