def poor_calories_counter(meal1, meal2, meal3):

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
    a = MC_CALORIES.get(meal1, 'item_name not found')
    b = MC_CALORIES.get(meal2, 'item_name not found')
    c = MC_CALORIES.get(meal3, 'item_name not found')
    return a + b + c


meal1 = "Hamburger"
meal2 = "French Fries"
meal3 = "Coca Cola"

print(poor_calories_counter(meal1, meal2, meal3))
