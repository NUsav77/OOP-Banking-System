import random


class Account:

    def __init__(self, account_number):
        self.account_number = account_number


class CheckingAccount(Account):
    balance = 0

    def __init__(self, account_number, pin):
        super().__init__(account_number)
        self.SavingAccount = SavingAccount
        self.pin = pin


    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, pin, amount):
        if pin == self.pin:
            self.balance -= print('Insufficient funds') if amount > self.balance else amount
        else:
            print('Invalid PIN')

    def transfer_to_saving(self, amount):
        if amount > self.balance:
            print('Insufficient funds')
        else:
            self.SavingAccount.balance += amount
            self.balance -= amount


class SavingAccount(Account):
    balance = 0

    def __init__(self, account_number):
        super().__init__(account_number)
        self.CheckingAccount = CheckingAccount

    def deposit(self, amount):
        self.balance += amount

    def transfer_to_checking(self, amount):
        if amount > self.balance:
            print('Insufficient funds')
        else:
            self.balance -= amount
            self.CheckingAccount.balance += amount


class CreditCardAccount(Account):
    remaining_limit = 0
    rating_to_apr = {'A': 0.5, 'B': 2.5, 'C': 5.0, 'F': None}

    def __init__(self, account_number, credit_rating):
        super().__init__(account_number)
        self.card_apr = CreditCardAccount.rating_to_apr.get(credit_rating)


def generate_account_num():
    """Generates an eleven digit account number

    :return: int
    """
    return random.randint(10000000000, 99999999999)


def generate_employee_id():
    """Generates a nine digit employee ID number

    :return: int
    """
    return random.randint(100000000, 999999999)
