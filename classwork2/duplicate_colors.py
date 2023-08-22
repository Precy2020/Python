def my_colour():
    colour1 = ["White", "Black", "Red"]
    colour2 = ["Red", "Black"]
    empty_list = []
    for index in colour1:
        for index2 in colour2:
            if index == index2:
                empty_list.append(index)
    return empty_list


print(my_colour())
