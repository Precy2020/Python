from bank_operation.account import Account


def test_add():
    account = Account("1", "precious", "1234")
    assert account.get_balance() == 0
    account.deposit(5000)
    assert account.get_balance() == 5000
