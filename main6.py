class Animal:
    def __init__(self, name):
        self.name = name

    def voice(self):
        print(f'{self.name} издает звук')

class Cat(Animal):
    def voice(self):
        Animal.voice(self)
        print('Meow')

class Dog(Animal):
    def voice(self):
        Animal.voice(self)
        print('Гав')


myCat = Cat('Барсик')
myDog = Dog('Шарик')

myCat.voice()
myDog.voice()