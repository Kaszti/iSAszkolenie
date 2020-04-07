class Zwierze():
    def hej(self):
        print('Heeee?!?')


class Czlowiek(Zwierze):
    def hej(self):
        print('Siema jestem czlowiek.')


class Student(Czlowiek):
    def hej(self):
        print('Panda 3')


class Profesor(Czlowiek):
    # def hej(self):
    #     print('Dzien dobry Panstwu')

    def inna(self):
        print('Inne przywitanie')


zwierze = Zwierze()
zwierze.hej()
profesor = Profesor()
profesor.hej()
profesor.inna()
czlowiek = Czlowiek()
czlowiek.hej()

# class Kot(Zwierze):
#     pass
#
#
# class Pies(Zwierze):
#     pass
#
#
# class Bokser(Pies):
#     pass
#
#
# class Jamnik(Pies):
#     pass
#
#