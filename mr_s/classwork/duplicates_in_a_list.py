def my_function(cars):
    empty = []
    for index in cars:
        if index != empty:
            empty.append(index)
    return empty


car = [1, 2, 3, 3, 8, 9]
print(my_function(car))
