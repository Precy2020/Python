card_number = str(input('Kindly enter your card number :) >> '))
types = []
length = []
collect = []


def card_number_validator():
    global card_number
    global collect

    for digit in card_number:
        collect = int(digit)
        print(collect)


card_number_validator()


def card_type_checker():
    global card_number
    global types
    global collect
    for _ in card_number:
        if card_number[0] == 4:
            types.append('Visa Card')
        elif card_number[0] == 5:
            types.append('Master Card')
        elif card_number[0] == 37:
            types.append('American Express Cards')
        elif card_number[0] == 6:
            types.append('Discover Cards')
        else:
            types.append('Invalid Card')
        return types


print(card_type_checker())


def card_number_length_checker():
    global collect
    global length
    for digits in collect:
        if 13 < digits > 16:
            length.append('Valid Card Number')
        else:
            length.append('Invalid Card Number')
        return length


print(card_number_length_checker())
