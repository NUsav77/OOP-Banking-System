import random
import users


class Account(users.Customer):
    def __init__(self, account_number, first_name, last_name):
        super().__init__(first_name, last_name)
        self.account_number = account_number


class CheckingAccount(Account):
    def __init__(self, account_number, balance):
        super().__init__(account_number)
        users.Customer.balance = balance


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
