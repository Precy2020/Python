"""WRITE A PYTHON PROGRAM THAT CONCATENATES ALL ELEMENTS IN A LIST INTO A STRING AND RETURNS IT"""


def concatenate_list_elements(lists):
    for index in lists:
        concatenate = lists[index] + lists[index]
        return concatenate


lister = [1, 2, 3, 4, 5]
print(concatenate_list_elements(lister))
