def is_number(number):
    try:
        float(number)
    except:
        print('To nie jest liczba hultaju!')
        return False
    else:
        print('To jest liczba')
        return True
