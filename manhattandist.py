def manhattan_distance(pointA, pointB):
    result = 0
    a = pointA[0]
    b = pointA[1]
    c = pointB[0]
    d = pointB[1]

    x = a - c
    y = b - d

    if x < 0:
        x = x - 2*x
    if y < 0:
        y = y - 2*y

    result = x + y
    return result


pointA = [1, 1]
pointB = [0, 3]

manhattan_distance(pointA, pointB)


def manhattan_distance1(pointA, pointB):
    return abs(pointA[0]-pointB[0]) + abs(pointA[1]-pointB[1])
