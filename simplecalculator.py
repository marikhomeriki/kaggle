

def simple_calculator(calculate):
    result = 0
    if len(calculate) != 3 or calculate[1] not in ['+', '-', '/', '*', '%']:
        if len(calculate) != 3:
            return "Please enter valid format: [Operand, Operator, Operand]"
        else:
            return "Please enter a valid operator [ +, -, /, *, % ]"

    a = calculate[0]
    b = calculate[2]
    if a.__contains__('.'):
        a = float(calculate[0])
    else:
        a = int(calculate[0])

    if b.__contains__('.'):
        b = float(calculate[2])
    else:
        b = int(calculate[2])

    if calculate[1] == '+':
        result = a + b
    elif calculate[1] == '-':
        result = a - b
    elif calculate[1] == '*':
        result = a * b
    elif calculate[1] == '/':
        result = a / b
    else:
        result = a % b

    return result


cal = ['9', '%', '2']  # 1
cal1 = ['5', '+', '5']  # 10
cal2 = ['10.5', '-', '5']  # 5.5
cal3 = ['8', '*', '8']  # 64
cal4 = ['1', '/', '4']  # 0.25
cal5 = ['9', '%', '2']  # 1
cal6 = ['1', '4']  # invalid
cal7 = ['1', '4', '5', '+']  # invalid
cal8 = ['1', '&', '5']  # invalid
print(simple_calculator(cal))
print(simple_calculator(cal1))
print(simple_calculator(cal2))
print(simple_calculator(cal3))
print(simple_calculator(cal4))
print(simple_calculator(cal5))
print(simple_calculator(cal6))
print(simple_calculator(cal7))
print(simple_calculator(cal8))
