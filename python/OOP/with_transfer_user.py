
# make_withdrawal(self, amount) - have this method decrease the user's balance by the amount specified
# display_user_balance(self) - have this method print the user's name and account balance to the terminal
# eg. "User: Guido van Rossum, Balance: $150
# BONUS: transfer_money(self, other_user, amount) - have this method decrease the user's balance by 
# the amount and add that amount to other other_user's balance


class User():
    def __init__(self,name):
        #here are class attributes
        self.name = name
        self.balance = 0.0

    def make_withdrawal(self, ammount):
        self.balance -= ammount
        return self

    def make_deposit(self, ammount):
        self.balance += ammount
        return self

    def display_user_balance(self):
        return (self.balance)
    
    def transfer_money(self, other_user, amount):
        other_user.make_deposit(amount)
        self.balance -= amount
        return self

newUser= User("Vicky")
secondUser = User("Laura")
print(newUser.make_deposit(100).make_deposit(200).display_user_balance())
print(secondUser.make_deposit(1000).make_deposit(20).make_deposit(30).make_withdrawal(5).display_user_balance())
