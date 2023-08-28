number1 = 0
number2 = 1
number3 = 50
for number in range(number3):
    print(f"{number}", end=' ')
    fibo = number1 + number2
    number3 = fibo
    # print(number3)
