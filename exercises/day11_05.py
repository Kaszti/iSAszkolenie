#properties

class Tajny_agent():
    def __init__(self, imie, nazwisko):
        self.__imie: str = imie
        self.__nazwisko: str = nazwisko
        self.__zarobki: float = 9999.00

    @property
    def imie(self):
        if self.__imie == None:
            return 'brak danych'
        else:
            return self.__imie[0].capitalize() + '*********'

    @imie.setter
    def imie(self, nowa_wartosc):
        self.__imie = nowa_wartosc

    @imie.deleter
    def imie(self):
        self.__imie = None

agent_1 = Tajny_agent('Tomek', 'Kowalski')
print(agent_1.imie)
agent_1.imie = 'Marek'
print(agent_1.imie)
del(agent_1.imie)
print(agent_1.imie)