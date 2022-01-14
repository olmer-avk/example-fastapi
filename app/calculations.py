
def add(a: int, b: int = 3):
    return a + b


class InsufficientFunds(Exception):
    pass


class BankAccount:
    def __init__(self, start_balance=0):
        self.balance = start_balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFunds("Insufficient funds")
        self.balance -= amount

    def collect_interests(self):
        self.balance *= 1.1
