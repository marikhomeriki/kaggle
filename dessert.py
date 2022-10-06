class Dessert:
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories

    def healthy(self):
        return self.calories < 200

    def delicious(self):
        return True


class JellyBean(Dessert):

    def __init__(self, name, calories, flavor):
        super().__init__(name, calories)
        self.flavor = flavor

    def delicious(self):
        if self.flavor is "licorice":
            return False
        else:
            return super().delicious()
