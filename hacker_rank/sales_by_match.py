def sock_selection(array: list):
    new = []
    empty_list = []
    empty_list2 = []
    for number in array:
        if number not in empty_list:
            empty_list.append(number)

        else:
            empty_list2.append(number)
    for num in empty_list2:
        if num not in new:
            new.append(num)

    print(empty_list2)
    return len(new)


arr = [1, 2, 3, 1, 3, 2, 1, 2]
print(sock_selection(arr))
