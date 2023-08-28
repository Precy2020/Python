"""WRITE A PYTHON PROGRAM THAT CHECKS WHETHER A SPECIFIED VALUE IS CONTAINED WITHIN A GROUP OF VALUES
TEST DATA:
3 -> [1, 5, 8, 3]: TRUE
-1 -> [1, 5, 8, 3]: FALSE"""


def number_check(number):
    lists = [1, 5, 8, 3]
    for numbers in lists:
        if number == numbers:
            return True
        else:
            return False


print(number_check(-1))
