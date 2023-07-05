print(f"\tNumbers\tSquares\tCubes\t")
numbers = 0
squares = 0
cubes = 0
for numbers in range(0, 6):
    squares = numbers * numbers
    cubes = numbers * numbers * numbers
    print(f"\t{numbers}\t\t{squares}\t\t{cubes}\t")
