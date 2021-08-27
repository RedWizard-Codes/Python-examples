import random
a=random.randrange(100000)
class BankAccount:
    accounts = []
    def __init__(self, int_rate, balance): 
        self.bank_id = a
        self.bank_name = "First National Dojo"
        self.balance = balance
        self.int_rate = int_rate
        BankAccount.accounts.append(self)
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdrawal(self, amount):
        if(self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print("Insufficient Funds: Charging a $5 fee")
            self.balance -= 5
        return self
    def transfer(self,user,amount):
        user.balance += amount
        self.balance -= amount
        return self
    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self
    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self
    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()

class User:
    def __init__(self,name,email):
        self.name = name
        self.email = email
        self.account = BankAccount(.01, 500)


Andres = User('Andres', 'email')
print(Andres.account.balance)
print(Andres.account.bank_name)
print(Andres.name)
Andres.savings = BankAccount(.01,3000)
Andres.savings.name= 'savings'

guido = User("guido", "email")
guido.bank_name = "Dojo Credit Union"
guido.name = "Guido"
print(guido.account.balance)
print(guido.account.bank_name)
print(guido.name)

monty = User('monty', 'email')
monty.name = "Monty"
# monty.transfer(guido,350)
print(monty.account.balance)
print(monty.name)
print(monty.account.bank_name)



guido.account.deposit(10).deposit(20).deposit(40).withdrawal(600).yield_interest()
monty.account.deposit(100).deposit(200).deposit(400).withdrawal(60).yield_interest()

BankAccount.print_all_accounts()

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# how do i make the guidobalance stay updated?
# transfer not working anymore and no idea why. it did before and it was in the bank class so no movement. mmmm
# tried to make a bank id. shit looks hard. ie. need to save to each a "random" number and not repeat, encrypt maybe, decryptor... we shall see later
