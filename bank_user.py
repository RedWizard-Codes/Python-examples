# make_withdrawal(self, amount) - have this method decrease the user's balance by the amount 
# specified

# display_user_balance(self) - have this method print the user's name and account balance 
# to the terminal
# eg. "User: Guido van Rossum, Balance: $150

# BONUS: transfer_money(self, other_user, amount) - have this method decrease the user's 
# balance by the amount and add that amount to other other_user's balance

# Practice creating a class and making instances from it
# Practice accessing the methods and attributes of different instances
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

class User:
    def __init__(self,name,email):
        self.name = name
        self.email = email
        self.balance = 0
        self.bank_name = "First National Dojo"
    def deposit(self, amount):
        self.balance += amount
    def make_withdrawal(self, amount):
        self.balance -= amount
    def transfer(self,user,amount):
        user.balance += amount
        self.balance -= amount

guido = User("guido", "email")
guido.bank_name = "Dojo Credit Union"
guido.name = "Guido"
guido.deposit(1000)
print(guido.balance)
print(guido.bank_name)
print(guido.name)

monty = User('monty', 'email')
monty.name = "Monty"
monty.deposit(1000)
monty.transfer(guido,350)
print(monty.balance)
print(monty.name)
print(monty.bank_name)
print(guido.balance)
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# how do i make the guidobalance stay updated?
# i tried to make a second class "bank" and i couldnt figure out how to reference a seperate class.