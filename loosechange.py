
def loose_change(cents):
    pennies = 1
    nickels = 5
    dimes = 10
    quarters = 25
    change = {
        "Nickels": 0,
        "Pennies": 0,
        "Dimes": 0,
        "Quarters": 0,
    }
    if cents <= 0:
        return change

    if type(cents) == float:
        cents = int(cents)

    while cents != 0:
        if cents >= quarters:
            q = int(cents/quarters)
            change["Quarters"] = q
            cents = cents - q*quarters
            print(cents)
        if cents >= dimes:
            d = int(cents/dimes)
            change["Dimes"] = d
            cents = cents - d*dimes
            print(cents)
        if cents >= nickels:
            n = int(cents/nickels)
            change["Nickels"] = n
            cents = cents - n*nickels
            print(cents)
        if cents >= pennies:
            p = int(cents/pennies)
            change["Pennies"] = p
            cents = cents - p*pennies
            print(cents)
        return change


cents = 56
cents1 = -435
cents2 = 4.935
cents3 = 130

print(loose_change(cents3))
