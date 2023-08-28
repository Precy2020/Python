
def even_and_odd_number_validator():
    try:
        user_input = int(input('Enter a number: '))
        if user_input % 2 == 0:
            print('The number inputted is a even number')
        elif user_input % 2 != 0:
            print('The number inputted is an odd number')
        else:
            print('Not valid')
    except ValueError:
        print('That is not a valid number')


even_and_odd_number_validator()
