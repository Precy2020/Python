def my_function(number):
    largest = number[0]
    for index in range(1, len(number)):
        if number[index] % 2 == 0 and number[index] > largest:
            largest = number[index]
            return largest


listed = [2, 8, 3, 5, 9, 6, 7]
print(my_function(listed))
