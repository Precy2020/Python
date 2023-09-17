from test import addition
from bank_operation.bank import Bank
from bank_operation.account import Account


def test_add():
    account = Account("1", "precious", "1234")
    assert 0 == account.get_balance()
    account.deposit(5000)
    assert 5000 == account.get_balance()
