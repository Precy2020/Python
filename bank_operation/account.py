class Account:
    balance = 0

    def __init__(self, account_number, account_name, pin):
        self.account_number = account_number
        self.account_name = account_name
        self.pin = pin

    def deposit(self, deposit):
        if deposit > 0:
            self.balance += deposit

    def get_balance(self):
        return self.balance

    def __is_valid_withdraw_private(self, withdraw):
        if self.balance >= withdraw > 0:
            return withdraw

    def __is_correct_pin_private(self, pins):
        if self.pin == pins:
            return True
        else:
            raise Exception('Not valid')

    def withdraw(self, withdraw, pins):
        if self.__is_valid_withdraw_private(withdraw):
            if self.__is_correct_pin_private(pins):
                self.balance = self.balance - withdraw

    def update_pin(self, old_pin, new_pin):
        if self.is_correct_pin_private(old_pin):
            self.pin = new_pin

    def get_account_number(self):
        return self.account_number
