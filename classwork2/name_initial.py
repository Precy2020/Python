def collect_name(name: str):
    newList = [name]
    for characters in newList:
        if characters.istitle():
            print(characters)


collect_name(input("Enter your name: "))
