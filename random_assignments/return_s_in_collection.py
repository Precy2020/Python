def collections(collection):
    name = {}
    count = 0
    for item in collection:
        if item[0] == 'S'.casefold():
            count += 1
            name[item] = 1
        if item[0] == 'S'.casefold():
            name[item] += 1

    return name


names = ['Samuel', 'samuel', 'glory', 'samuel', 'sola', 'shally', 'blessed']
print(collections(names))
