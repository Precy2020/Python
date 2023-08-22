customer_name = 0
purchased_item = 0
quantity = 0
amount = 0
add = 0


def user_input():
    global customer_name
    global purchased_item
    global quantity
    global amount
    global add

    customer_name = input('What is the customer\'s Name? ')
    purchased_item = input('What did the user buy? ')
    quantity = input('How many pieces? ')
    amount = input('How much per unit? ')
    add = input('Add more items? ')

    if add == 'yes'.casefold():
        return user_input()
    if add == 'no'.casefold():
        return input('How much discount will he/she get? ')
    else:
        return 'invalid input'


user_input()
