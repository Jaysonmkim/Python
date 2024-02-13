class Fruits:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show(self):
        print(f"I love eating {self.name} and it costs {self.price}")

myobject = Fruits("Passions", "Ksh30")
myobject.show()

myobject2 = Fruits("Bananas", "Ksh15")
myobject2.show()

myobject3 = Fruits("Mangoes", "Ksh25")
myobject3.show()

myobject4 = Fruits("Watermelons", "Ksh70")
myobject4.show()

myobject5 = Fruits("Apples", "Ksh25")
myobject5.show()
