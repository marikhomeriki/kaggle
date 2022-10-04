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

MEALS = {
    "Happy Meal": ["Cheese Burger", "French Fries", "Coca Cola"],
    "Best Of Big Mac": ["Big Mac", "French Fries", "Coca Cola"],
    "Best Of McChicken": ["McChicken", "Salad", "Sprite"]
}


def advanced_calories_counter(meal):
    for m in meal:
        if m not in MC_CALORIES and m not in MEALS:
            return f"{m} not found"

    calories = 0
    for i in range(len(meal)):
        if meal[i] not in MEALS:
            calories += MC_CALORIES[meal[i]]
        else:
            meals = MEALS[meal[i]]
            for j in range(len(meals)):
                calories += MC_CALORIES[meals[j]]
    return calories


meal = ["French Fries", "Happy Meal", "Sprite", "Best Of McChicken"]

advanced_calories_counter(meal)
