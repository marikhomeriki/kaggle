class User(object):
    def __init__(self, name, balance, checking_account):
        self.name = name
        self.balance = balance
        self.checking_account = checking_account

    def withdraw(self, amount):
        if self.balance > amount:
            balance = self.balance - amount
            return f"Jeff has {balance}."
        else:
            raise ValueError("No sufficient balance")


Jeff = User('Jeff', 70, True)

print(Jeff.withdraw(71))
