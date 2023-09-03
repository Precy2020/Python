from bank_operation.account import Account


class Bank:

    def __init__(self):
        self.accounts = []

    def register(self, first_name, last_name, pin):
        account = Account(self.generate_account_number(), first_name + '' + last_name, pin)
        self.accounts.append(account)

    def generate_account_number(self):
        return self.accounts.__len__() + 1

    def find_account(self, account_number) -> Account:
        for search_account in self.accounts:
            if search_account.get_account_number() == account_number:
                return search_account

    def can_deposit(self, account_number, deposit):
        self.find_account(account_number).deposit(deposit)

    def get_balance(self, account_number):
        return self.find_account(account_number).get_balance()

    def can_withdraw(self, account_number, withdraw, pin):
        self.find_account(account_number).withdraw(withdraw, pin)
