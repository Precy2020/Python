def collections(collection):
    name = {' ': 0}
    for item in collection:
        if item[0].casefold() == 's':
            name[item] += 1
    return name.items()


names = ['Samuel', 'glory', 'sola', 'shally', 'blessed']
print(collections(names))
