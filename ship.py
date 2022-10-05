class Ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew

    def is_worth_it(self):
        return self.draft - self.crew * 1.5 > 20


titanic = Ship(20, 15)
print(titanic.draft-titanic.crew*1.5 > 20)
print(titanic.crew*1.5)
x = titanic.is_worth_it()
print(x)
