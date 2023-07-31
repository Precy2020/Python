def my_function(cars):
    emptyList = []
    for index in cars:
        if index is not emptyList:
            emptyList += [index]
    return emptyList


car = ['toyota', 'camry', 'honda', 'benz', 'corolla', 'benz']
print(my_function(car))
