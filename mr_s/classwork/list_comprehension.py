number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


even = [index for index in number if index % 2 == 0]
print(even)

odd = [index for index in number if index % 2 != 0]
print(odd)

square = [index ** 2 for index in number]
print(square)

add = [index + 2 for index in number]
print(add)
