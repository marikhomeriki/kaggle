class Student:

    def __init__(self, name, fives, tens, twenties):
        self.name = name
        self.fives = fives
        self.tens = tens
        self.twenties = twenties

    def wealth(self):
        return self.fives*5 + self.tens*10 + self.twenties*20

    def compare(self, other):
        if self.wealth() > other.wealth():
            return self.name
        else:
            return other.name


one = Student('Amy', 5, 6, 7)
two = Student('Bilbo', 3, 4, 5)
three = Student('Chuck', 2, 3, 4)
four = Student('Diane', 1, 2, 3)

print(one.compare(two))
