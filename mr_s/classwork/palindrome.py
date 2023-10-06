# strings = input('Enter a strings: ')


def my_string(string):
    if string == string[:: - 1]:
        return string
    else:
        return 'Not a palindrome'


print(my_string('praise'))
