def password(string):
    sum_uppers = 0
    sum_digits = 0
    sum_lowers = 0
    if len(string) < 8:
        return False

    for c in string:
        if c.isupper():
            if sum_uppers == 0:
                sum_uppers += 1
            continue

        if c.isdigit():
            if sum_digits == 0:
                sum_digits += 1
            continue
        if c.islower():
            if sum_lowers == 0:
                sum_lowers += 1
            continue
    return sum_uppers+sum_lowers+sum_digits == 3


pass1 = "AbcdefGhijKlmnopQRsTuvwxyZ1234567890"

print(password(pass1))
