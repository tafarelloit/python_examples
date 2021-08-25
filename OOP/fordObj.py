class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def __getitem__(self, i):
        return self.cars[i]

    def __repr__(self):
        return f"<Garage {self.cars}>"

    def __str__(self):
        return f"Garage with {len(self.cars)} cars."

ford = Garage()
ford.cars.append("Fiesta")
ford.cars.append("Mustang")

print(len(ford))

print(ford[0])
"""
It is possible iterate over because the
two methods len and getitem were implemented
the __repr__ function is used when debugging the code
the __str__ function is invoked when printing the object

if you implemented __repr__ only then it will be used for printing purposes.
"""
for car in ford:
    print(car)

#invoke __str__
print(ford)
