def list_and_tuple():
    user_input = [input("Enter comma separated number: ")]
    empty_list = []
    empty_tuple = []
    for digits in user_input:
        empty_tuple.append(digits)
        print(tuple(empty_tuple))
        empty_list.append(digits)
        return empty_list


print(list_and_tuple())
