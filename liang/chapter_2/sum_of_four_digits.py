digits = int(input("Enter four digits: "))

first_digit = digits // 1000
second_digit = digits % 1000 // 100
third_digit = digits % 1000 % 100 // 10
forth_digit = digits % 1000 % 100 % 10

add = first_digit + second_digit + third_digit + forth_digit
print("The sum of the above digits is ",  add)
