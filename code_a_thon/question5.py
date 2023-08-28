def reverse_username():
    firstname = input('Enter your first  name: ')
    lastname = input('Enter your last name: ')

    first_reverse = firstname[:: - 1]
    last_reverse = lastname[:: - 1]

    print(first_reverse)
    print(last_reverse)


reverse_username()
