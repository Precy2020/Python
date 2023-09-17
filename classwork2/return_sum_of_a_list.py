def sum_list(lists, value):
    for index in lists:
        for indexes in range(len(lists)):
            if index + index == value:
                return indexes


list1 = [5, 4, 9, 7, 2, 0]
print(sum_list(list1, 12))


# def create_tuple(l1, l2):
#     new_list = []
#     for numbers in l1, l2:
#         new_list.append(tuple(numbers))
#
#     return new_list
#
#
# first_list = [1, 3, 6, 8, 9, 0]
# second_list = [0, 9, 8, 6, 3, 1]
# print(create_tuple(first_list, second_list))
