from operator import truediv


def lovefunc(flower1, flower2):
    love_sum = (flower1 + flower2) % 2
    if love_sum == 1:
        return True
    else:
        return False


print(lovefunc(4, 5))
