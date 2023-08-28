def my_string(string):
    if string.casefold() == string[:: - 1].casefold():
        return True
    else:
        return False


print(my_string('MaDam'))
