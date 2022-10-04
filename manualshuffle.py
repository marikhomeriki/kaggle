import random


def manual_shuffle(arr):

    for i in range(len(arr)):
        ran = random.randint(0, len(arr)-1)
        val = arr[i]
        val2 = arr[ran]
        arr[ran] = val
        arr[i] = val2

    return arr


arr = list(range(10))
print(manual_shuffle(arr))
