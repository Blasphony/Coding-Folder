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


indi= BankAccount(.03,30000)
tamaki= BankAccount(.10,1000)

indi.deposit(10).deposit(20).deposit(40).withdraw(600).yield_interest().display_account_info()
tamaki.deposit(100).deposit(200).deposit(400).withdraw(60).yield_interest().display_account_info()

BankAccount.print_all_accounts()