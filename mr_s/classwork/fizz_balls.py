def fizz_balls(numbers):
    for number in range(numbers):
        if number % 3 == 0 and number % 5 == 0:
            print('fizz buzz')
        elif number % 3 == 0:
            print('fizz')
        elif number % 3 == 0:
            print('buzz')
        else:
            print(number)


fizz_balls(101)
