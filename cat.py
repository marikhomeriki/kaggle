class Cat:
    def __init__(self):
        self.age = 1
        self.color = 'brown'
        self.weight = 5

    def age_10_years(self):
        self.age = 10
        return self

    def gain_weight(self):
        self.weight = 20
        return self

    def turn_grey(self):
        self.color = 'grey'


cat = Cat()
print(f"My {cat.age} year old cat weighs {cat.weight} pounds and is {cat.color}.  Come back in a few years and see how he is doing.")

x = cat.gain_weight()
print(x)

cat.age_10_years().gain_weight().turn_grey()
print("--------------------10 years later----------------------")
print(f"My {cat.age} year old cat now weighs {cat.weight} pounds and is {cat.color}")
