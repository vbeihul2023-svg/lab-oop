class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Fish(Animal):
    pass

animals = [Dog(), Cat(), Fish()]
for animal in animals:
    result = animal.speak()
    print(f"{animal.__class__.__name__}: {result}")

