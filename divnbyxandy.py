def is_divisible(n, x, y):
    if n % x == 0 and n % y == 0:
        return True
    else:
        return False


n = 3
x = 1
y = 3

print(is_divisible(n, x, y))
