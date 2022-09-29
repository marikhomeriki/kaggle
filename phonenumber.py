def create_phone_number(numbers):
    a = "".join(map(str, numbers))
    number = '(' + a[0:3] + ')'+'-' + a[3:6] + '-' + a[6:]
    return number


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(create_phone_number(numbers))
