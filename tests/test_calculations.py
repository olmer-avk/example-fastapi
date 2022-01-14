import pytest
from app.calculations import add, BankAccount, InsufficientFunds


@pytest.mark.parametrize("x, y, res", [
    (3, 2, 5),
    (7, 1, 8),
    (12, 4, 16)
])
def test_add(x, y, res):
    assert add(x, y) == res


@pytest.fixture
def zero_bank_acc():
    return BankAccount()


@pytest.fixture
def bank_acc():
    return BankAccount(50)


def test_bank_account_init(bank_acc):
    assert bank_acc.balance == 50


def test_bank_account_init_default(zero_bank_acc):
    assert zero_bank_acc.balance == 0


def test_bank_account_deposit(bank_acc):
    bank_acc.deposit(30)
    assert bank_acc.balance == 80


def test_bank_account_with_draw(bank_acc):
    bank_acc.withdraw(20)
    assert bank_acc.balance == 30


def test_bank_account_collect_interests(bank_acc):
    bank_acc.collect_interests()
    assert round(bank_acc.balance, 2) == 55


@pytest.mark.parametrize("deposited, withdrew, res", [
    (200, 100, 100),
    (50, 10, 40),
    (1200, 200, 1000)
])
def test_bank_transactions(zero_bank_acc, deposited, withdrew, res):
    zero_bank_acc.deposit(deposited)
    zero_bank_acc.withdraw(withdrew)
    assert zero_bank_acc.balance == res


def test_insufficirnt_funds(bank_acc):
    with pytest.raises(InsufficientFunds):
        bank_acc.withdraw(200)

