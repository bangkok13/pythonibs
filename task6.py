class Animal:
    _counter = 0
    def __init__(self, voice):
        Animal._counter += 1
        self.voice = voice
        pass


class Cat(Animal):
    def voice(self):
        print('gg')

class Dog(Animal):
    def voice(self):
        print('')

class Mouse(Animal):
    def voice(self):
        print('')

a = Cat.voice()
a

Cat.voice('john')
Dog.voice('joy')
Mouse.voice('jerry')