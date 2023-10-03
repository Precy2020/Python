def second_largest(string: str):
    new_list = []
    for strings in string:
        if strings.isdigit():
            new_list.append(int(strings))


print(second_largest(input("input here: ")))
