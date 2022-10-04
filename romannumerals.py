def roman_to_int(roman):
    ROMANS = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    result = 0
    for i in range(len(roman)):
        if i > 0 and ROMANS[roman[i]] > ROMANS[roman[i-1]]:
            result += ROMANS[roman[i]] - 2*ROMANS[roman[i-1]]
        else:
            result += ROMANS[roman[i]]
    return result


roman = 'XLVIII'

print(roman_to_int(roman))
