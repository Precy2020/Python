def my_function(cars):
    emptyList = []
    for index in cars:
        if index is not emptyList:
            emptyList.append(index)
    return emptyList


car = ['green', 'red', 'red', 'green', 'purple', 'yellow']
print(my_function(car))

