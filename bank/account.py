class Account:
    balance = 0

    def __init__(self, account_number, account_name, pin):
        self.account_number = account_number
        self.account_name = account_name
        self.pin = pin

    def deposit(self, deposit):
        global balance
        if deposit > 0:
            balance = deposit + 1

    def get_balance(self):
        global balance
        return balance

    def withdraw(self, pins):
        if self.pin == pins:
            return True
        else:
            raise Exception('Not valid')



