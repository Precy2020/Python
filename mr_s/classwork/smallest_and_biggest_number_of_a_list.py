numbers = [10, 20, 50, 40, 30]
largest = numbers[0]
smallest = numbers[0]
for index in range(1, len(numbers)):
    if numbers[index] > largest:
        largest = numbers[index]
    if numbers[index] < smallest:
        smallest = numbers[index]

print(f"{smallest} is the smallest")
print(f"{largest} is the largest")

