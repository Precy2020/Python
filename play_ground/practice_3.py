'''A guessing game
Determine a winning number
let it run for like 20times until the user's input is correct'''
import random
num1 = random.randint(1, 5)
counter = 1

while counter <= 6:
    num = int(input("Guess the number: "))

    if num == num1:
        print("You won $1000")
        break
    else:
        print('Try again')
        counter = counter + 1








