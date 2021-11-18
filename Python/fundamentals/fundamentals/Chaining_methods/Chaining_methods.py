class Person:
    def __init__(self,name, amount):
        self.amount = amount
        self.name = name
    def make_deposit(self,input):
        self.amount+=input
        return self
    def make_withdrawl(self,input):
        self.amount-=input
        return self
    def display_user_balance(self):
        print("user: ",self.name,"balance:", self.amount)

stan = Person("stan",25)
indi = Person("indi",31)
winston = Person('winston',42)

stan.make_deposit(10).make_deposit(15).make_deposit(25).make_withdrawl(30).display_user_balance()


indi.make_deposit(10).make_deposit(30).make_withdrawl(5).make_withdrawl(23).display_user_balance()

winston.make_deposit(10).make_withdrawl(20).make_withdrawl(1).make_withdrawl(3).display_user_balance()