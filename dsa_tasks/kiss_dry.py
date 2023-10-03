def dry_kiss(string: str):
    newList = []
    list_ = [6, 2, 3, 4, 1, 0, 5]
    for index in string:
        newList.append(index)
        for numbers in list_:
            for characters in newList:
                for chars in range(len(newList)):
                    if numbers == chars:
                        print(characters)


dry_kiss("kissdry")
