import re


def password_validator(user=input('Enter your password dear :)>> ')):
    pattern = "[a-zA-Z0-9]{8}"
    if re.search(pattern, user):
        print(user)
    else:
        print('Password is invalid')


password_validator()
