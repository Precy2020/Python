from bank_operation.bank import Bank


class Main:
    lamour_bank = Bank()

    @staticmethod
    def write(prompt):
        return input(prompt + "\n>>> ")

    @staticmethod
    def show(message):
        print(message)

    @staticmethod
    def main_menu():
        user_option = """
            ()()()()()()()()()()()()()()()()
            >>>Welcome to Lamour Bank :)<<<
            ()()()()()()()()()()()()()()()()
            1). Create Account.
            2). Deposit.
            3). Withdraw.
            4). Transfer.
            5). Balance
            6). Exit.
            ()()()()()()()()()()()()()()()()
            """
        user_input = Main.write(user_option)
        match user_input:
            case '1':
                Main.create_account()
            case '2':
                Main.deposit()
            case '3':
                Main.withdraw()
            case '4':
                Main.transfer()
            case '5':
                Main.balance()
            case '6':
                Main.exit()
            case _:
                Main.show("Invalid selection!!!")

    @staticmethod
    def balance():
        account_number = Main.write("Put in your account number: ")
        balance = str(Main.lamour_bank.get_balance(account_number))
        Main.show("Your balance is " + balance)
        Main.main_menu()

    @staticmethod
    def create_account():
        first_name = Main.write("Enter your first name:> ")
        last_name = Main.write("Enter your last name:> ")
        pin = Main.write("Enter a prefer pin:> ")
        Main.validate(first_name, last_name, pin)
        Main.main_menu()

    @staticmethod
    def validate(first_name, last_name, pin):
        if not first_name or first_name.isdigit():
            Main.show("First name can not be empty or a digit!!!")
            Main.main_menu()
        if not last_name or last_name.isdigit():
            Main.show("Last name can not be empty or a digit!!!")
            Main.main_menu()
        if not pin or pin.isalpha():
            Main.show("Pin can not be empty or an Alphabet!!!")
            Main.main_menu()
        else:
            account_number = Main.lamour_bank.register(first_name, last_name, pin)
            Main.show("Welcome dear you are now our Customer :)!!!")
            Main.show("AccountNumber: " + account_number)
            Main.main_menu()

    @staticmethod
    def transfer():
        from_account = Main.write("Enter the sender's account number: ")
        to_account = Main.write("Enter the receiver's account number: ")
        transfer_amount = Main.write("How much: ")
        pin = Main.write("Enter sender's pin: ")
        Main.lamour_bank.bank_can_transfer(from_account, to_account, int(transfer_amount), pin)
        Main.main_menu()

    @staticmethod
    def deposit():
        try:
            account_number = Main.write("Put in your account number: ")
            deposit_amount = Main.write("How much do you want to deposit?-> ")
            Main.lamour_bank.find_account(account_number).deposit(int(deposit_amount))
            Main.show(f"{deposit_amount} deposited successfully!!")
            Main.main_menu()
        except ValueError as e:
            Main.show(str(e))

    @staticmethod
    def withdraw():
        try:
            account_number = Main.write("Put in your account number: ")
            withdraw_amount = Main.write("How much do you want to withdraw?-> ")
            pin = Main.write("Put in your pin: ")
            Main.lamour_bank.find_account(account_number).withdraw(int(withdraw_amount), pin)
            Main.show("Money withdrawn successfully!")
            Main.main_menu()
        except ValueError as e:
            Main.show(str(e))

    @staticmethod
    def exit():
        exit(0)


if __name__ == "__main__":
    Main.main_menu()
