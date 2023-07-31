def is_leap(years):
    leap = False
    leap2 = True
    if years % 400 == 0:
        return leap2
    else:
        return leap


year = int(input())
print(is_leap(year))