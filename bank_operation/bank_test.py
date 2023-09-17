import unittest
from bank_operation.bank import Bank


class BankTest(unittest.TestCase):
    bank = Bank();
    registered = bank.register("Favour", "Ochonogor", "1234")

    def test_that_account_can_register(self):
        self.bank = Bank()
        self.bank.register("Favour", "Ochonogor", "1234")

    def test_that_bank_can_find_account(self):
        self.bank.find_account('1')
        self.assertIsNotNone(self.bank.generate_account_number())

    # def test_that_bank_can_deposit(self):
    #     self.bank.can_deposit('1', 2000)
    #     self.assertEqual(2000, self.bank.get_balance('1'))

    # def test_that_bank_can_withdraw(self):
    #     self.bank.can_withdraw('1', 3000, "1234")
    #     self.assertEqual(0, self.bank.get_balance('1'))



