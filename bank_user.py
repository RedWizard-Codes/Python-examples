class User:
    def __init__(self,name,email):
        self.name = name
        self.email = email

guido = User("guido", "email")
monty = User('monty', 'email')
Andres = User('Andres', 'email')

import random
a=random.randrange(100000)
class BankAccount:
    def __init__(self, int_rate, balance): 
        self.bank_id = a
        self.bank_name = "First National Dojo"
        self.balance = 0
        self.int_rate = .001
    def deposit(self, amount):
        self.balance += amount
    def withdrawal(self, amount):
        self.balance -= amount
    def transfer(self,user,amount):
        user.balance += amount
        self.balance -= amount
    # def display_account_info(self):
        # your code here
        # print(self.BankAccount)
    # def yield_interest(self):

Andres=BankAccount(.05,400)


guido = User("guido", "email")
guido.bank_name = "Dojo Credit Union"
guido.name = "Guido"
guido.deposit(1000)
guido.deposit(1000)
guido.deposit(1000)
guido.withdrawal(550)
print(guido.balance)
print(guido.bank_name)
print(guido.name)

monty = User('monty', 'email')
monty.name = "Monty"
monty.deposit(1000)
monty.deposit(46000)
monty.withdrawal(300)
monty.withdrawal(300)
monty.withdrawal(300)
monty.withdrawal(300)
monty.transfer(guido,350)
print(monty.balance)
print(monty.name)
print(monty.bank_name)
print(guido.balance)


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# how do i make the guidobalance stay updated?
# i tried to make a second class "bank" and i couldnt figure out how to reference a seperate class.
# i need a yield interest def? i dont even know where to start
