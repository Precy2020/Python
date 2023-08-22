class Oop2:
    color = 'red'

    def __init__(self, first_parameter, second_parameter):
        self.first = first_parameter
        self.second = second_parameter

    @property
    def first(self):
        return self.__first

    @first.setter
    def first(self, value):
        if value < 0:
            raise ValueError('value cannot be negative')
        self.__first = value

    @property
    def second(self):
        return self.__second

    @second.setter
    def second(self, value):
        if value < 0:
            raise ValueError('value cannot be negative')
        self.__second = value

    def draw(self):
        print(f"drawing from first {self.__first} to {self.__second}")

    def __str__(self):
        return f"({self.first}, {self.second})"

    def __add__(self, other):
        return (self.__first + other.first), (self.__second + other.second)

    # def evaluate(self, me):
    #     return (self.__first + me.first), (self.__second + me.second)


Oop2.color = "green"
point1 = Oop2(1, 2)
point2 = Oop2(1, 2)

print(point1 + point2)
