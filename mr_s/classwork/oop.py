class Oop:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def draw(self):
        print('Anything')

    def __str__(self):
        return f"({self.first}, {self.second})"


p1 = Oop(3, 4)
p2 = Oop(3, 8)

print(p1)
print(p2)
