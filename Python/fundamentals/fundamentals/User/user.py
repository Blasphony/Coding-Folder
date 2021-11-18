class Person:
    def __init__(self,name, amount):
        self.amount = amount
        self.name = name
    def make_deposit(self,input):
        self.amount+=input
    def make_withdrawl(self,input):
        self.amount-=input
    def display_user_balance(self):
        print("user: ",self.name,"balance:", self.amount)

stan = Person("stan",25)
indi = Person("indi",31)
winston = Person('winston',42)

stan.make_deposit(10)
stan.make_deposit(15)
stan.make_deposit(25)
stan.make_withdrawl(30)
stan.display_user_balance()

indi.make_deposit(10)
indi.make_deposit(30)
indi.make_withdrawl(5)
indi.make_withdrawl(23)
indi.display_user_balance()

winston.make_deposit(10)
winston.make_withdrawl(20)
winston.make_withdrawl(1)
winston.make_withdrawl(3)
winston.display_user_balance()