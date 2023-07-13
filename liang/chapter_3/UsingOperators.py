number = int(input("Enter a number: "))
print("Is 10 divisible by 5 and 6?", (number % 5 == 0) and (number % 6 == 0))
print("Is 10 divisible by 5 or 6?", (number % 5 == 0) or (number % 6 == 0))
print("Is 10 divisible by 5 or 6? but not both", (number % 5 == 0) ^ (number % 6 == 0))
