MC_CALORIES = {
    "Hamburger": 250,
    "Cheese Burger": 300,
    "Big Mac": 540,
    "McChicken": 350,
    "French Fries": 230,
    "Salad": 15,
    "Coca Cola": 150,
    "Sprite": 150
}


def poor_calories_counter(meal1, meal2, meal3):

    keys = list(MC_CALORIES.keys())
    if meal1 not in keys:
        return f'{meal1} not found'
    if meal2 not in keys:
        return f'{meal2} not found'
    if meal3 not in keys:
        return f'{meal3} not found'

    a = MC_CALORIES.get(meal1)
    b = MC_CALORIES.get(meal2)
    c = MC_CALORIES.get(meal3)
    return a + b + c


meal1 = "Shrimp"
meal2 = "French Fries"
meal3 = "Salad"

print(poor_calories_counter(meal1, meal2, meal3))
