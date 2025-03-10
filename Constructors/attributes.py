class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def info(self):
        print(f"{self.make} {self.model}")

my_car = Car("Toyota", "Camry")
my_car.info()
print(my_car.make)