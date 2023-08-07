def game():
    number_selected = int(input('Guess a number between 1 - 10 \n'))
    if number_selected == 5:
        print('You won')
    if number_selected > 10:
        print('too high')
        int(input('Guess a number between 1 - 10 \n'))
    elif number_selected < 1:
        print('too low')
        int(input('Guess a number between 1 - 10 \n'))


game()
