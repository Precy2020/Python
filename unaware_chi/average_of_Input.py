total = 0
average = 1
for love in range(1, 11):
    score = int(input(">>> "))
    total = score + total
    average = score / average
print(average)
