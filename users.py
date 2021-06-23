import accounts
import mysql.connector
import secrets

cnx = mysql.connector.connect(user='admin', password=secrets.my_sql_password,
                              host='127.0.0.1',
                              database='bank_mini_project')

class User:

    def __init__(self, first_name, last_name, ssn='000-00-0000'):
        self.first_name = first_name.lower()
        self.last_name = last_name.lower()
        self.ssn = [print('invalid ssn') if len(ssn.replace('-', '')) != 9 else ssn]

    @property
    def fullname(self):
        return f'{self.first_name} {self.last_name}'.title()

    @fullname.setter
    def fullname(self, name):
        first_name, last_name = name.split(' ')
        self.first_name = first_name
        self.last_name = last_name


class Customer(User):
    is_active = False
    credit_evaluated = False

    credit_score_dict = {
        'A': range(830, 900),
        'B': range(750, 830),
        'C': range(670, 750),
        'F': range(0, 670),
    }

    def __init__(self, first_name, last_name, account_num=0, pin=0, credit_score=None):
        super().__init__(first_name, last_name)
        self.checking_account_num = None if Customer.is_active is False else account_num
        self.pin = None if Customer.is_active is False else pin
        self.credit_score = credit_score
        self.credit_rating = None
        self.card_apr = None
        self.checking = None
        self.checking_account = None
        self.loan_num = None

    @property
    def customer_info(self):
        return f'{self.fullname}\nAccount # {self.checking_account_num}'

    def create_checking(self):
        pin = int(input('Please enter a 4 digit PIN: '))
        pin_confirm = int(input('Reconfirm 4 digit PIN: '))
        self.pin = print('Invalid PIN') if len(str(pin)) != 4 | pin != pin_confirm else pin
        if self.pin:
            self.checking_account_num = accounts.generate_account_num()
            self.is_active = True if self.pin else False
            self.has_checking_account = True if self.pin else False
            self.checking = accounts.CheckingAccount(self.checking_account_num, self.pin)
            print(f'Checking Account # {self.checking_account_num} created')

    def create_saving(self):
        if not isinstance(self.checking, accounts.CheckingAccount): # self.has_checking_account is False:
            print('Must create checking account first')
        else:
            self.saving_account_num = accounts.generate_account_num()
            self.saving = accounts.SavingAccount(self.saving_account_num)
            self.has_saving_account = True
            print(f'Saving Account # {self.saving_account_num} created')

    def get_credit_rating(self, credit_score):
        self.credit_score = credit_score
        for rating, score in self.credit_score_dict.items():
            if credit_score in score:
                self.credit_rating = rating
                self.credit_evaluated = True
                print(f'Rating of {self.credit_rating}')

    def create_credit_card(self):
        if self.credit_evaluated is False:
            print('Must get credit rating first')
        elif self.has_checking_account is False:
            print('Must have a checking account to apply for a credit card')
        elif self.credit_rating == 'F':
            print('Not eligible for credit card')
        else:
            self.credit_card_num = accounts.generate_account_num()
            self.credit_card = accounts.CreditCardAccount(self.credit_card_num, self.credit_rating)
            self.card_apr = self.credit_card.card_apr
            print(f'Credit card approved\n\tCard # {self.credit_card_num}\n\tAPR rating: {self.card_apr}%')

    def create_loan(self):
        if not isinstance(self.checking, accounts.CheckingAccount):
            print('Must open a checking account')
        elif self.credit_evaluated is False:
            print('Must get credit rating first')
        elif self.credit_rating == 'F':
            print('Not eligible for loan')
        else:
            self.loan_num = accounts.generate_account_num()
            self.loan = accounts.LoanAccount(self.loan_num, self.credit_rating)
            print(f'Load approved\n\tLoan Account # {self.loan_num}\n\tAPR: {self.loan.loan_apr}%\n\tTotal Loan Amount: ${self.loan.loan_amount}')


class Employee(User):
    is_active = False

    def __init__(self, first_name, last_name, branch_location):
        super().__init__(first_name, last_name)
        self.employee_id = accounts.generate_employee_id()
        self.branch_location = branch_location
        self.is_active = True
        print(f'Employee ID # {self.employee_id}')

    @property
    def employee_info(self):
        return f'{self.fullname}/nEmployee ID # {self.employee_id}'


steven = Customer('steven', 'nodalo')
steven.create_checking()
