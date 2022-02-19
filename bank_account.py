class Bankaccount:
    accounts = []
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        Bankaccount.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if self.balance < amount:
            self.balance -= 5
            print("Insufficient funds: Charging $5 fee")
        else:
            self.balance -= amount
        return self
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self
    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self
    @classmethod
    def print_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()

ron = Bankaccount(.02, 100)
cassidy = Bankaccount(.03, 500)

ron.deposit(100).deposit(50).deposit(325).withdraw(150).yield_interest().display_account_info()
cassidy.deposit(500).deposit(50).withdraw(200).withdraw(100).withdraw(25).withdraw(255).yield_interest().display_account_info()

Bankaccount.print_accounts()
