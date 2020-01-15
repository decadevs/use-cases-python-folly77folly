# Document 1 use case of an interface in python
# That is define an interface using the abstract base class module
# Add at least 3 entities that can implement the interface in a way that make sense.

#This application is possible for when creating different users where its standard
# they must always have login and logout time
import abc
from datetime import datetime

class Interface(abc.ABC):

    @abc.abstractmethod
    def log_in():
         pass

    @abc.abstractmethod
    def log_out():
         pass

    # @abc.abstractmethod
    # def login_time():
    #     pass

    # @abc.abstractmethod
    # def logout_time():
    #     pass

class Admin(Interface):
    def __init__(self, email, password):
        self.email = email
        self.password = password
        # self.login_time = datetime.now()
    
    def log_in(self):
        if self.email == self.email and self.password == self.password:
            # self.login_time = datetime.now()
            return f'login Successful by {self.email} at {datetime.now()}'

    def log_out(self):
        if self.email == self.email and self.password == self.password:
            return f'{self.email} thank you hope to have you back'

class CustomerCare(Interface):
    def __init__(self, email, password):
        self.email = email
        self.password = password
        # self.login_time = datetime.now()
    
    def log_in(self):
        if self.email == self.email and self.password == self.password:
            # self.login_time = datetime.now()
            return f'login Successful by {self.email} at {datetime.now()}'

    def log_out(self):
        if self.email == self.email and self.password == self.password:
            return f'{self.email} thank you hope to have you back'
        

class Accounts(Interface):
    def __init__(self, email, password):
        self.email = email
        self.password = password
        # self.login_time = datetime.now()
    
    def log_in(self):
        if self.email == self.email and self.password == self.password:
            # self.login_time = datetime.now()
            return f'login Successful by {self.email} at {datetime.now()}'

    def log_out(self):
        if self.email == self.email and self.password == self.password:
            return f'{self.email} thank you hope to have you back'



admin1=Admin('gbolahan@gmail.com','pass')
user1=CustomerCare('akeem@gmail.com','pass')
accounts1=Accounts('alimot@gmail.com','pass')
print(admin1.log_in())
print(user1.log_in())
print(accounts1.log_in())