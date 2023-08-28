def reverse_a_string():
    string = "Glory"
    emptyList = []
    for characters in string[:: - 1]:
        emptyList.append(characters)
    return emptyList


print(reverse_a_string())
