def age_d(age_h):
    if age_h <= 2 and age_h > 0:
      age_dog = age_h * 10.5
      print(f'Wiek psa w psich latach wynosi: {age_dog}')
    elif age_h > 2:
        age_dog_1 = 2 * 10.5
        age_dog_2 = (age_h - 2) * 4
        age_dog_sum = age_dog_1 + age_dog_2
        print(f'Wiek psa w psich latach wynosi: {age_dog_sum}')


