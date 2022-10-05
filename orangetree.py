import random


class OrangeTree:
    def __init__(self, age=0, height=0, fruit=0, dead=0):
        self.age = age
        self.height = height
        self.fruit = fruit
        self.dead = dead

    def one_year_passes(self):
        if self.age < 100:
            self.age += 1
        else:
            self.dead = True

        if self.age > 50:
            self.dead = self.age/100 > random.random()

        if self.age <= 10:
            self.height += 1

        if not self.dead:
            if self.age > 5 and self.age < 10:
                self.fruit = 100
            elif self.age < 15:
                self.fruit = 200
            else:
                self.fruit = 0

    def pick_fruit(self):
        self.fruit -= 1
