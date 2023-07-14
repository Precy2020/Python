numbers = [10, 20, 30, 40, 50]
largest = numbers[0]
smallest = numbers[0]
for x in range(1, len(numbers)):
    if numbers[x] > largest:
        largest = numbers[x]
    if numbers[x] < smallest:
        smallest = numbers[x]

print(f"{smallest} is the smallest")
print(f"{largest} is the largest")

