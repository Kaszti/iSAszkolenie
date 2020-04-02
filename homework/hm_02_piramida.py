def piramida():
    try:
        height = int(input('Podaj wysokosc piramidy: '))
        i = 1
        m = 1
        width = height * 2 - 1
        while i <= height:
            x = m * '#'
            y = x.center(width)
            print(y)
            i += 1
            m += 2
    except:
        print('Wysokosc piramidy musi byc liczba calkowita')
        piramida()