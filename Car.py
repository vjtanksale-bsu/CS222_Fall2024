class Car:
    wheels = 4
    def __init__(self, make, model):
        self.make = make
        self.model = model
def main():
    car0 = Car("Ford", "F-150")
    car1 = Car("Toyota", "Camry")
    car1.make = "Chevrolet"
    print(car1.make)
    print(car0.make)
    print(car1.wheels)
    print(car0.wheels)
    Car.wheels = 5
    print(car1.wheels)
    print(car0.wheels)
main()