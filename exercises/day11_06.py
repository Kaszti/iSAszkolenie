class Car():
    def __init__ (self, brand, color, capacity, price_netto):
        self.brand: str = brand
        self.color: str = color
        self.capacity: float = capacity
        self.price: float = price_netto
    vat_value = 23
    __spread = 10

    def price_brutto(self):
        price_s = self.price + (self.__spread / 100) * self.price
        price_b = price_s + (self.vat_value / 100) * price_s
        return price_b

    def presentation(self):
        return f'Kupiles auto marki {self.brand} w kolorze {self.color} o pojemności silnika {self.capacity} litra za {self.price_brutto()} zł brutto'

    @classmethod
    def spread(cls):
        return cls.__spread

    @classmethod
    def set_spread(cls, new_spread):
        if new_spread > 5 and new_spread < 15:
            cls.__spread = new_spread
        else:
            print('Wrong value, setting default')
            return cls.__spread

ford = Car('FORD', 'BIAŁY', 5.0, 100000)
audi = Car('AUDI', 'CZARNY', 2.4, 80000)
print(ford.presentation())
print(audi.presentation())
