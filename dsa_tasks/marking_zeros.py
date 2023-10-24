def mark_zeros(array: list):
    for number in array:
        if number == 0:
            array.remove(number)
            array.append(number)
    return array


_list = [4, 0, 3, 0, 2, 0, 4, 10, 0]

print(mark_zeros(_list))
