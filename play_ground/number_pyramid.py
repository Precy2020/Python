number = 7

for pyramid in range(1 + number):
    for column in range(pyramid, number):
        print(' ', end=' ')
    for column in range(1,pyramid ):
        print(f"{column}", end=' ')
    for column in range(1, pyramid + 1):
        print(f"{column}", end=" ")
    print()
