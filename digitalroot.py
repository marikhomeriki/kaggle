def digital_root(n):
    if n < 10:
        return n
    while n > 9:
        sum = 0
        digits = [int(x) for x in str(n)]
        length = len(digits)
        for i in range(length):
            sum += digits[i]
        n = sum

    return sum


def digital_root1(n):
    if n < 10:
        return n
    else:
        digital_root1(sum(map(int, str(n))))


# return n if n < 10 else digital_root1(sum(map(int, str(n))))


n = 16
n0 = 8
n1 = 942
n2 = 132189
n3 = 493193
print(digital_root1(n1))
# print(digital_root(n1))
# print(digital_root(n2))
# print(digital_root(n3))
# print(digital_root(n0))
