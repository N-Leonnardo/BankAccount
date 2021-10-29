class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount
    def display_account_info(self):
        print('Balance:' + str(+self.balance))

    def yield_interest(self):
        if (self.balance>0):
            self.balance = self.balance + (self.balance* 0.01)

guido = BankAccount(100)
guida = BankAccount(10)

guido.deposit(100)
guido.deposit(100)
guido.withdraw(50)
guido.yield_interest()
guido.display_account_info()

guida.deposit(200)
guida.withdraw(10)
guida.withdraw(10)
guida.withdraw(10)
guida.withdraw(10)
guida.yield_interest()
guida.display_account_info()

