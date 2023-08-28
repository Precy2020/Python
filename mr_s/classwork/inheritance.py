class Animal:
    def __init__(self):
        number_of_nose = 1

    def eat(self):
        print("eating")


class Dog(Animal):
    def __init__(self):
        self.number_of_legs = 4
        super().__init__()

    @property
    def number_of_legs(self):
        return self.number_of_legs

    def walk(self):
        print("walking")


class Fish(Animal):
    def swim(self):
        print("swimming")
