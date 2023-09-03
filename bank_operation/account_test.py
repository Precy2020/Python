import unittest
from bank_operation.account import Account
from bank_operation.invalid_input import InvalidInput


class AccountTest(unittest.TestCase):
    def test_account_can_deposit(self):
        account = Account("1", "precious", "1234")
        self.assertEquals(0, account.get_balance())
        account.deposit(5000)
        self.assertEqual(5000, account.get_balance())

    def test_account_can_withdraw(self):
        account = Account("1", "precious", "1234")
        account.deposit(5000)
        self.assertEqual(5000, account.get_balance())
        account.withdraw(1500, "1234")
        self.assertEqual(3500, account.get_balance())

    def test_that_customer_cannot_deposit_negative_amount(self):
        account = Account("1", "precious", "1234")
        self.assertRaises(InvalidInput, account.deposit(-5000))


    def test_that_pin_can_be_updated(self):
        account = Account("1", "precious", "1234")
        account.update_pin("1234", "4321")
        account.deposit(5000)
        self.assertEqual(5000, account.get_balance())
        account.withdraw(1500, "4321")
        self.assertEqual(3500, account.get_balance())

    def test_that_customer_cannot_withdraw_more_than_balance(self):
        account = Account("1", "precious", "1234")
        account.update_pin("1234", "4321")
        account.deposit(5000)
        self.assertEqual(5000, account.get_balance())
        account.withdraw(1500, "4321")
        self.assertEqual(3500, account.get_balance())
