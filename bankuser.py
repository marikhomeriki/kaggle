class User(object):
    def __init__(self, name, balance, checking_account):
        self.name = name
        self.balance = balance
        self.checking_account = checking_account

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance = self.balance - amount
            return f"{self.name} has {self.balance}."
        else:
            raise ValueError("No sufficient balance")

    def add_cash(self, amount):

        self.balance = self.balance + amount
        return f"{self.name} has {self.balance}."

    def check(self, other, amount):
        if not other.checking_account:
            raise ValueError()
        other.withdraw(amount)
        self.add_cash(amount)
        return f"{self.name} has {self.balance} and {other.name} has {other.balance}."


Jeff = User('Jeff', 70, True)
Joe = User('Joe', 70, True)

print(Jeff.withdraw(2))
print(Joe.check(Jeff, 50))
print(Jeff.check(Joe, 80))
print(Jeff.add_cash(20))
