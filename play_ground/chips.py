def greater_than(number1, number2, number3, number4):
    overall = number1
    if number2 > number1:
        overall = number2
    else:
        overall = number1
        if number3 > number4:
            overall = number3
        else:
            overall = number4
        print(overall)


greater_than(20, 10, 20, -1)


def smallest(number1, number2, number3, number4):
    little = number1
    if number2 < number1:
        little = number2
    else:
        little = number1
        if number3 < number4:
            little = number3
        else:
            little = number4
        print(little)


smallest(0, 30, 7, 8)
