
x = 1
y = 1
z = 2
n = 3

# test1 = [i for i in range(x+1)]
# test = [[(i for i in range(x+1)), (j for j in range(y+1)),
#         (k for k in range(z+1))]]
# print(test1)
test2 = []
test3 = []
# test2.append([i for i in range(x+1), 1])

for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            test3.append([i, j, k])


print(test3)
print(test2)

mari = [[i, j, k] for k in range(z+1) for j in range(y+1)
        for i in range(x+1) if i + j + k != n]
mari = sorted(mari)
print(mari)
