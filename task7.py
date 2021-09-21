class Animal:
    count = 0
    def voice(self):
        pass


class Cat(Animal):
    def voice(self):
        Animal.count += 1
        print('Мяу')

class Dog(Animal):
    def voice(self):
        Animal.count += 1
        print('Гав')

class Mouse(Animal):
    def voice(self):
        Animal.count += 1
        print('ПИ пИ ПИ')

Cat.voice('john')
Dog.voice('joy')
Mouse.voice('jerry')
print(Animal.count)