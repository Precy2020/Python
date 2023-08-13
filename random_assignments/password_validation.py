import re
import string


def password_validator(user=input('Enter your password dear :)>> ')):
    special_character = string.punctuation
    pattern = r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$"
    if re.search(pattern, user):
        return "greatness!!!"
    if len(user) < 8:
        print("password should be up to eight characters long")
        password_validator(user=input('Enter your password dear :)>> '))
    if not re.match('[a-z]', user):
        print('Password must contain a lowercase at least')
        password_validator(user=input('Enter your password dear :)>> '))
    if not re.match('[A-Z]', user):
        print('Password must contain a uppercase at least')
        password_validator(user=input('Enter your password dear :)>> '))
    if not re.match('[\d]', user):
        print('Password must contain a number at least')
        password_validator(user=input('Enter your password dear :)>> '))
    if not re.match(special_character, user):
        print('Password must contain a special character at least')
        password_validator(user=input('Enter your password dear :)>> '))


password_validator()
