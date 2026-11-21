from abc import ABC, abstractmethod

class Account(ABC):
    @abstractmethod
    def access_account(self):
        pass
    
class BankAccount(Account):
    def access_account(self):
        print('Accessing Bank Account')
        
class BankAccountProxy(Account):
    def __init__(self, permission):
        self.user_permission = permission
        self.account = BankAccount()
        
    def access_account(self):
        if self.user_permission == 'authentic_user':
            self.account.access_account()
        else:
            print('Access Denied')
        
client1 = BankAccountProxy('authentic_user')
client1.access_account()

client2 = BankAccountProxy('user')
client2.access_account()