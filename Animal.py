class Animal:
    def __init__(self, name):
        self.name = name
    def MakeSound(self):
        print(self.name + " is making a sound")
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    def MakeSound(self):
        print(f"{self.name} is barking")
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color
    def MakeSound(self):
        print(self.name + " is meowing")
def main():
    dog = Dog("Buddy", "Golden Retriever")
    #dog.MakeSound()
    AnimalSound(dog)
    cat = Cat("Whiskers", "Tabby")
    #cat.MakeSound()
    AnimalSound(cat)
def AnimalSound(animal):
    animal.MakeSound()
main()











