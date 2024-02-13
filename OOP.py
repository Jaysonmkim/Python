class Car:
    def __init__(self, make, model, year, colour):
        self.make=make
        self.model=model
        self.year=year
        self.colour=colour
    def onyesha(self):
        print(f"My dream car is {self.make} and my model is"
        f" {self.model} manufactured in {self.year} which is colour {self.colour}")
myobj=Car("Lamborghini","Urus",2019,"Yellow")
myobj.onyesha()
myobj2=Car("Dodge","Challenger",2018,"Black")
