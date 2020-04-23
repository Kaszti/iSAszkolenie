def changer():
    try:
        value = float(input('Podaj kwote jaka chcesz rozmienic: '))
        if value % 5 == 0:
            ch_5_0 = int(value / 5)
            print(f'Liczba monet o nominale 5: {ch_5_0}')
        else:
            ch_5_1 = int(value // 5)
            r_5 = value % 5
            print(f'Liczba monet o nominale 5: {ch_5_1}')
            if r_5 % 2 == 0:
                ch_2_0 = int(r_5 / 2)
                print(f'Liczba monet o nominale 2: {ch_2_0}')
            else:
                ch_2_1 = int(r_5 // 2)
                r_2 = r_5 % 2
                print(f'Liczba monet o nominale 2: {ch_2_1}')
                if r_2 % 1 == 0:
                    ch_1_0 = int(r_2 / 1)
                    print(f'Liczba monet o nominale 1: {ch_1_0}')
                else:
                    ch_1_1 = int(r_2 // 1)
                    r_1 = r_2 % 1
                    print(f'Liczba monet o nominale 1: {ch_1_1}')
                    if r_1 % 0.5 == 0:
                        ch_05_0 = int(r_1 / 0.5)
                        print(f'Liczba monet o nominale 0.5: {ch_05_0}')
                    else:
                        ch_05_1 = int(r_1 // 0.5)
                        r_05 = r_1 % 0.5
                        print(f'Liczba monet o nominale 0.5: {ch_05_1}')
                        if r_05 % 0.2 == 0:
                            ch_02_0 = int(r_05 / 0.2)
                            print(f'Liczba monet o nominale 0.2: {ch_02_0}')
                        else:
                            ch_02_1 = int(r_05 // 0.2)
                            r_02 = r_05 % 0.2
                            print(f'Liczba monet o nominale 0.2: {ch_02_1}')
                            if r_02 % 0.1 == 0:
                                ch_01_0 = int(r_02 / 0.1)
                                print(f'Liczba monet o nominale 0.1: {ch_01_0}')
                            else:
                                ch_01_1 = int(r_02 // 0.1)
                                r_01 = r_02 % 0.1
                                print(f'Liczba monet o nominale 0.1: {ch_01_1}')
                                if r_01 % 0.05 == 0:
                                    ch_005_0 = int(r_01 / 0.05)
                                    print(f'Liczba monet o nominale 0.05: {ch_005_0}')
                                else:
                                    ch_005_1 = int(r_01 // 0.05)
                                    r_005 = r_01 % 0.05
                                    print(f'Liczba monet o nominale 0.05: {ch_005_1}')
                                    if r_005 % 0.02 == 0:
                                        ch_002_0 = int(r_005 / 0.02)
                                        print(f'Liczba monet o nominale 0.02: {ch_002_0}')
                                        print('Liczba monet o nominale 0.01: 0')
                                    elif r_005 % 0.02 != 0:
                                        ch_002_1 = int(r_005 // 0.02)
                                        print(f'Liczba monet o nominale 0.02: {ch_002_1}')
                                        print('Liczba monet o nominale 0.01: 1')
    except:
        print('Kwota jest liczba.')
        changer()