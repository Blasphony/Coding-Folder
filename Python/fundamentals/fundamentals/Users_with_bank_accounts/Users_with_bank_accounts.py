class BankAccount:
    # class attribute
    all_accounts = []
    def __init__(self, int_rate,balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
    
    def deposit(self,input):
        self.balance+=input
        return self

    def withdraw(self,input):
        if (self.balance - input) >=0:
            self.balance-=input
        else:
            print("Insufficient Funds: charging a $5 fee")
            self.balance -=5
        return self
    # class method to get current account
    def display_account_info(self):
        print(f"Balance is {self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self

    @classmethod
    def print_all_accounts(cls):
        for all_account in cls.all_accounts:
            all_account.display_account_info()

class User:
    def __init__(self,name):
        self.name= name
        self.all_accounts = {
            "indi" : BankAccount(.02,1000),
            "tamaki" : BankAccount(.05,3000)
        }

    # other methods
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    def make_withdraw(self, amount):
        if self.account_balance >= 0:
            self.account_balance -= amount
        else:
            print("Sadge")
        return self
    def display_user_balance(self):
        print(f"Balance is {self.balance}")
        return self
        







