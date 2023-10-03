class Account:
    def __init__(self, account_number, account_name, pin):
        self.balance = 0
        self.account_number = account_number
        self.account_name = account_name
        self.pin = pin

    def get_pin(self):
        return self.pin

    def get_account_name(self):
        return self.account_name

    def deposit(self, deposit):
        if deposit > 0:
            self.balance += deposit
        else:
            raise ValueError("Deposit amount must be greater than 0")

    def get_balance(self):
        return self.balance

    def withdraw(self, withdraw, entered_pin):
        if self.is_valid_withdrawal(withdraw) and self.is_correct_pin(entered_pin):
            if self.balance >= withdraw:
                self.balance -= withdraw
            else:
                raise ValueError("Insufficient funds for withdrawal")
        else:
            raise ValueError("Invalid withdrawal amount or incorrect PIN")

    def is_correct_pin(self, entered_pin):
        return self.pin == entered_pin

    def is_valid_withdrawal(self, withdraw):
        return withdraw > 0

    def update_pin(self, old_pin, new_pin):
        if self.is_correct_pin(old_pin):
            self.set_pin(new_pin)
        else:
            raise ValueError("Incorrect Old Pin")

    def set_pin(self, new_pin):
        if len(new_pin) == 4 and new_pin.isdigit():
            self.pin = new_pin
        else:
            raise ValueError("Pin must be a 4-digit number")

    def get_account_number(self):
        return self.account_number

    def get_account(self):
        return f"Account{{account_name='{self.account_name}', account_number='{self.account_number}', pin='{self.pin}'}}"

