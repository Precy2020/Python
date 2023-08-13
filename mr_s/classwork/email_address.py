import re


def email_validator(email):
    pattern = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

    for mail in email:
        if not re.search(pattern, mail) and email[0] == '@':
            return 'Not valid'
        else:
            return 'valid'


emails = ['@ochonogor84@gmail.com']

print(email_validator(emails))
