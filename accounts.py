import random


class Account:

    def __init__(self, account_number):
        self.account_number = account_number


class CheckingAccount(Account):
    balance = 0

    def __init__(self, account_number, pin):
        super().__init__(account_number)
        self.saving_account = None
        self.pin = pin

    def deposit(self, amount):
        old_bal = self.balance
        self.balance += amount
        print(f'Previous Balance: ${old_bal}\nDeposit amount: ${amount}\nNew Balance: ${self.balance}')

    def withdraw(self, pin, amount):
        if pin == self.pin:
            self.balance -= print('Insufficient funds') if amount > self.balance else amount
        else:
            print('Invalid PIN')

    def transfer_to_saving(self, amount):
        if not isinstance(self.saving_account, SavingAccount):
            print('Must create a saving account')
        elif amount > self.balance:
            print('Insufficient funds')
        else:
            self.saving_account.balance += amount
            self.balance -= amount


class SavingAccount(Account):
    balance = 0

    def __init__(self, account_number):
        super().__init__(account_number)
        self.checking_account = None

    def deposit(self, amount):
        self.balance += amount

    def transfer_to_checking(self, amount):
        try:
            if amount > self.balance:
                print('Insufficient funds')
            else:
                self.balance -= amount
                self.checking_account.balance += amount
        except NameError:
            print('Invalid input')
        except TypeError:
            print('Must pass integer')


class CreditCardAccount(Account):
    remaining_limit = 0
    rating_to_apr = {'A': 2.5, 'B': 5.25, 'C': 15.0, 'F': None}
    card_apr = None

    def __init__(self, account_number, credit_rating):
        super().__init__(account_number)
        CreditCardAccount.card_apr = CreditCardAccount.rating_to_apr[credit_rating]


class LoanAccount(Account):
    remaining_balance = 0
    rating_to_apr = {'A': 0.5,
                     'B': 2.5,
                     'C': 5.0,
                     'F': None}
    loan_apr = None
    loan_amount = None

    def __init__(self, account_number, credit_rating):
        super().__init__(account_number)
        self.loan_amount = self.get_loan_amount(credit_rating)
        self.loan_apr = LoanAccount.rating_to_apr[credit_rating]


    def get_loan_amount(self, apr):
        apr_to_amount = {'A': 100000,
                         'B': 50000,
                         'C': 25000}
        return apr_to_amount[apr]


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
