class User:		
    def __init__(self,name,email):
        self.name = name
        self.email = email
        self.account = Bankaccount(int_rate= .02, account_balance = 0)

    def make_withdrawl(self, amount):
        self.account.account_balance-= amount
        return self
    def make_deposit(self, amount):
        self.account.account_balance += amount
        return self
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account.account_balance}")
        return self
    def transfer_money(self, other_user, amount):
        self.account.withdraw-= amount
        other_user.account.deposit += amount
        return self

class Bankaccount:
    accounts = []
    def __init__(self, int_rate, account_balance):
        self.int_rate = int_rate
        self.account_balance = account_balance
        Bankaccount.accounts.append(self)

    def deposit(self, amount):
        self.account_balance += amount
        return self
    def withdraw(self, amount):
        if self.account_balance < amount:
            self.account_balance -= 5
            print("Insufficient funds: Charging $5 fee")
        else:
            self.account_balance -= amount
        return self
    def display_account_info(self):
        print(f"Balance: ${self.account_balance}")
        return self
    def yield_interest(self):
        if self.account_balance > 0:
            self.account_balance += (self.account_balance * self.int_rate)
        return self
    @classmethod
    def print_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()

ron = User("Ron", "ron@gmail.com")

ron.make_deposit(1000)
ron.make_withdrawl(100)
ron.display_user_balance()
