import accounts


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
    checking_account = False
    saving_account = False

    def __init__(self, first_name, last_name, account_num=0, pin=0):
        super().__init__(first_name, last_name)
        self.checking_account_num = None if Customer.is_active is False else account_num
        self.pin = None if Customer.is_active is False else pin

    @property
    def customer_info(self):
        return f'{self.fullname}\nAccount # {self.checking_account_num}'

    def create_checking(self):
        pin = int(input('Please enter a 4 digit PIN: '))
        self.pin = print('Invalid PIN') if len(str(pin)) != 4 else pin
        if self.pin:
            self.checking_account_num = accounts.generate_account_num()
            self.is_active = True if self.pin else False
            self.checking = accounts.CheckingAccount(self.checking_account_num, self.pin)
            print(f'Checking Account # {self.checking_account_num} created')
            
    def create_saving(self):
        self.saving_account_num = accounts.generate_account_num()
        self.saving = accounts.SavingAccount(self.saving_account_num)
        print(f'Saving Account # {self.saving_account_num} created')

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