class C():
    def witaj(self):
        print('Jestem C')


class B():
    def witaj(self):
        print('Jestem B')


class D(B, C):
    def witaj(self):
        print('Jestem D')


class Z():
    pass

D().witaj()
obiekt_D = D()
print(isinstance(obiekt_D, D))
print(isinstance(obiekt_D, B))
print(isinstance(obiekt_D, C))
print(isinstance(obiekt_D, Z))
# obiekt = D() analogiczne do chainingu
# obiekt.witaj()