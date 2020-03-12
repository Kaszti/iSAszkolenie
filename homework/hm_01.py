# Przeliczanie Celsjusza na Fahrenheita
# TC = input('Podaj temperaturę w stopniach celsjusza: ')
# TF = (9/5)*float(TC)+32
# print('TF = (9/5)*TC+32')
# print('Temperatura w stopniach Fahrenheita jest równa: ' + str(TF))


#Stopnie Fahrenheita na Celsjusza
# TF = input('Podaj temperaturę w stopniach Fahrenheita: ')
# TC = (5/9)*float(TF)-(160/9)
# print('TC = (5/9)*TF-(160/9)')
# print('Temperatura w stopniach Celsjusza jest równa: ' + str(TC))


#Obliczanie pola powierzchni koła
# R = input('Podaj promień koła w milimetrach: ')
# print('P = pi*(R**2)')
# P = 3.14*(float(R)**2)
# print('Pole powierzchni koła wynosi: ' + str(P) + ' [mm]')


#Pierwsza i ostatnia cyfra
# Number = input("Podaj dowolną liczbę: ")
# if str(Number[0]) == str('-'):
#     print('Pierwsza cyfra to: ' + str(Number[1]) + ', a ostatnia cyfra to: ' + str(Number[-1]))
# else:
#     print('Pierwsza cyfra to: ' + str(Number[0]) + ', a ostatnia cyfra to: ' + str(Number[-1]))


#Rysowanie prostokąta
#Z racji tego, że operujemy na liczbach całkowitych ze względu na rysowanie prostokąta za pomocą znaków
#proszę o podanie długości podstawy i boku jako liczby całkowitej, inaczej wyskoczy bład.
#Niestety miałem masę pracy w weekend więc nie bawiłem, się w robienie warunków i program nie wyświetli
#komunikatu, że wpisano złą wartość.
# l_base = input('Podaj długość podstawy: ')
# l_side = input('Podaj długość boku: ')
# l_base_w = int(l_base) - 2
# l_side_w = int(l_side) - 2
# print('+' + l_base_w*'-' + '+')
# for user in range(0, l_side_w):
#     print('|' + l_base_w*' ' + '|')
# print('+' + l_base_w*'-' + '+')


#przeliczanie liczby zapisanej w formacie binarnym na dziesiętny
# length_check = True
# Number_b = input('Podaj liczbę zapisaną w formacie binarnym (6 znaków, tylko 0 lub 1): ')
# if len(Number_b) != 6:
#     print('Miało być 6 znaków')
#     length_check = False
# for i in range(0, len(Number_b)):
#     if int(Number_b[i]) !=0 and int(Number_b[i]) !=1:
#         print('System binarny zawiera tylko 0 i 1')
#         length_check = False
# if length_check == True:
#     Number_d = int(Number_b[0]) * 32 + int(Number_b[1]) * 16 + int(Number_b[2]) * 8 + int(Number_b[3]) * 4 + int(
#         Number_b[4]) * 2 + int(Number_b[5]) * 1
#     print('Liczba w zapisie binarnym: ' + Number_b)
#     print('Liczba w zapisie dziesiętnym: ' + str(Number_d))


#Rozpoznawanie parzystości
# Number = input('Podaj liczbę całkowitą: ')
# Parity_check = int(Number) % 2
# if Parity_check == 0:
#     print('Podana liczba jest parzysta! :D')
# else:
#     print('Podana liczba jest nieparzysta! :(')



#Podzielność przez 3 lub 5 lub 7
# Number = input('Podaj liczbę całkowitą: ')
# Divisibility_3 = int(Number) % 3
# if Divisibility_3 == 0:
#     print('Podana liczba jest podzielna przez 3.')
# else:
#     print('Podana liczba nie jest podzielna przez 3')
# Divisibility_5 = int(Number) % 5
# if Divisibility_5 == 0:
#     print('Podana liczba jest podzielna przez 5.')
# else:
#     print('Podana liczba nie jest podzielna przez 5')
# Divisibility_7 = int(Number) % 7
# if Divisibility_7 == 0:
#     print('Podana liczba jest podzielna przez 7.')
# else:
#     print('Podana liczba nie jest podzielna przez 7')

#Podzielność przez 3 i 5 i 7
# Number = input('Podaj liczbę całkowitą: ')
# Dividend = 3*5*7
# Divisibility = int(Number) % Dividend
# if Divisibility == 0:
#     print('Liczba jest podzielna przez 3 i 5 i 7.')
# else:
#     print('Liczba nie jest podzielna przez 3 i 5 i 7.')


#Sprawdzanie przestępczości roku (taka gra słów :D)
# Year = input('Podaj rok jaki chciałbyś/chciałabyś sprawdzić.')
# Divisibility_4 = int(Year) % 4
# Divisibility_100 = int(Year) % 100
# Divisibility_400 = int(Year) % 400
# if Divisibility_4 == 0 and Divisibility_100 !=0:
#     print('Podany rok jest przestępny.')
# elif Divisibility_400 == 0:
#     print('Podany rok jest przestępny.')
# else:
#     print('Podany rok nie jest przestępny.')
