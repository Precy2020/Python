from bank_operation.account import Account


class Bank:
    def __init__(self):
        self.accounts = []

    def register(self, first_name, last_name, pin):
        account_number = str(len(self.accounts) + 1)
        account = Account(account_number, f"{first_name} {last_name}", pin)
        self.accounts.append(account)
        return account_number

    def generate_account_number(self):
        return str(len(self.accounts) + 1)

    def find_account(self, account_number):
        for search in self.accounts:
            if search.get_account_number() == account_number:
                return search
        raise ValueError("Invalid account")

    def can_deposit(self, account_number, deposit):
        self.find_account(account_number).deposit(deposit)

    def get_balance(self, account_number):
        return self.find_account(account_number).get_balance()

    def can_withdraw(self, account_number, withdraw, pin):
        self.find_account(account_number).withdraw(withdraw, pin)

    def bank_can_transfer(self, source_account_number, destination_account_number, amount, pin):
        try:
            source_account = self.find_account(source_account_number)
            destination_account = self.find_account(destination_account_number)

            if source_account is None or destination_account is None:
                raise ValueError("Invalid source or destination account number")

            if source_account.get_balance() < amount:
                raise ValueError("Insufficient funds for the transfer")

            source_account.withdraw(amount, pin)
            destination_account.deposit(amount)
            print("Transfer successful")
        except ValueError as e:
            print(f"Error: {e}")