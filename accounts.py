import random


class Account:

    def __init__(self, account_number):
        self.account_number = account_number


class CheckingAccount(Account):
    checking_balance = 0

    def __init__(self, account_number, pin):
        super().__init__(account_number)
        self.pin = pin
        self.saving_balance = None

    def deposit(self, amount):
        self.checking_balance += amount

    def withdraw(self, pin, amount):
        if pin == self.pin:
            self.checking_balance -= print('Insufficient funds') if amount > self.checking_balance else amount
        else:
            print('Invalid PIN')

    def transfer_to_saving(self, amount):
        if amount > self.checking_balance:
            print('Insufficient funds')
        else:
            self.saving_balance += amount
            self.checking_balance -= amount


class SavingAccount(Account):
    saving_balance = 0

    def __init__(self, account_number):
        super().__init__(account_number)
        self.checking_balance = None

    def deposit(self, amount):
        self.saving_balance += amount

    def transfer_to_checking(self, amount):
        if amount > self.saving_balance:
            print('Insufficient funds')
        else:
            self.saving_balance -= amount
            self.checking_balance += amount


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
