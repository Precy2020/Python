import re


def sum_string_numeric(string: str):
    regex = re.compile('[@_!#$%^&*()\-<>?/}{~:]')
    newList = []
    add = 0
    for character in string:
        if character.isnumeric() and regex.match(character):
            newList.append(int(character))
    for number in newList:
        add += number
    return add


print(sum_string_numeric("bod1o7d-5"))
