number = int(input('Enter a value: '))
a = number // 10000
b = number % 10000 // 1000
c = number % 10000 % 1000 // 100
d = number % 10000 % 1000 % 100 // 10
e = number % 10000 % 1000 % 100 % 10 // 1

print(f" {a}, {b}, {c}, {d}, {e}")