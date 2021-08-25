class Currency:
    def __init__(self, amount):
        self.amount = amount

    def __repr__(self):
        return f"<Currency {self.amount:.2f}>"
    
    @classmethod
    def from_sum(cls, value1, value2):
        return cls(value1+value2)

class Euro(Currency):
    def __init__(self, amount):
        super().__init__(amount)
        self.symbol = "&"

    def __repr__(self):
        return f"<Euros {self.symbol}{self.amount:.2f}>"

class Dolar(Currency):
    def __init__(self, amount):
        super().__init__(amount)
        self.symbol = "$"

    def __repr__(self):
        return f"<Dolar {self.symbol}{self.amount:.2f}>"


euros = Euro.from_sum(15.789, 34.458)

print(euros)


dolars = Dolar.from_sum(55.678, 9.999)

print(dolars)
