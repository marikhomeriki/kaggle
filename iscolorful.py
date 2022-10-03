def is_colorful(num):
    digits = [int(x) for x in str(num)]
    length = len(digits)

    if length == 1:
        return True

    for i in range(length-1):
        digits.append(digits[i]*digits[i+1])
    return len(set(digits)) == len(digits)


num = 236
is_colorful(num)
