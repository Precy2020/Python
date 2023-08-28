def is_leap(years):
    leap = False
    leap2 = True
    if years % 4 == 0 and years % 100 != 0 or years % 400 == 0:
        return leap2
    else:
        return leap


year = int(input())
print(is_leap(year))
