import math


def litres(time):
    return math.floor(time*0.5)


def litres1(time):
    return int(time*0.5)


time = 1

print(litres1(time))

print(1*0.5)
print(int(1*0.5))
print(1 // 2)
x = 10 // 3
print(f"This is {x}")

print(litres2(time))
