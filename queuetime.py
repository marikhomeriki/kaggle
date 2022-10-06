def queue_time(customers, n):
    sum = 0
    if len(customers) == 0:
        return 0
    elif len(customers) == 1:
        return customers[0]

    if n == 1:
        for i in range(len(customers)):
            sum += customers[i]
        return sum
    if n > len(customers):
        return sorted(customers)[len(customers)-1]


customers = [2, 2, 3, 3, 4, 4]
n = 2

print(queue_time(customers, n))
