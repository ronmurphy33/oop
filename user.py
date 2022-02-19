# declare a class and give it name User
class User:		
    def __init__(self,name,email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_withdrawl(self, amount):
        self.account_balance-= amount
        return self
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account_balance}")
        return self
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self

guido = User("Guido","guido@gmail.com")
monty = User("Monty", "monty@gmail.com")

guido.make_withdrawl(100)
guido.display_user_balance()

ron = User("Ron","ronmurphy33@gmail.com")
cassidy = User("Cassidy","cdm@gmail.com")
maddie = User("Maddie", "maddie@gmail.com")

maddie.make_deposit(5000).make_deposit(100).make_deposit(55).make_withdrawl(150).display_user_balance()

cassidy.make_deposit(1000).make_deposit(500).make_withdrawl(12).make_withdrawl(300).display_user_balance()

ron.make_deposit(3000).make_withdrawl(300).make_withdrawl(50).make_withdrawl(1500).display_user_balance()

ron.transfer_money(maddie,1000)

ron.display_user_balance()
maddie.display_user_balance()


