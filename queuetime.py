def queue_time(customers, n):
    queue = [0] * n
    for i in customers:
        queue.sort()
        queue[0] += i

    return max(queue)


customers = [10, 2, 3, 3, 3]
n = 2

print(queue_time(customers, n))
