def my_corn(joy):
    for row in range(joy):
        for column in range(row + 1):
            print("*", end=" ")
        for column in range(row, joy):
            print("", end=" ")
        for column in range(row, joy):
            print("", end=" ")
        for column in range(row, joy):
            print("*", end=" ")
        for column in range(row + 1):
            print("", end=" ")
        for column in range(row + 1):
            print("", end=" ")
        for column in range(row + 1):
            print("", end=" ")
        for column in range(row + 1):
            print("", end=" ")
        for column in range(row, joy):
            print("*", end=" ")
        for column in range(row, joy):

            print("", end=" ")
        for column in range(row, joy):
            print("", end=" ")
        for column in range(row + 1):
            print("*", end=" ")
        print()


my_corn(10)
my_corn(10)
my_corn(10)

