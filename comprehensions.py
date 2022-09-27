
x = 1
y = 1
z = 2
n = 3

result = [[i, j, k] for k in range(z+1) for j in range(y+1)
          for i in range(x+1) if i + j + k != n]
result = sorted(result)
print(result)


test3 = []

for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            test3.append([i, j, k])


print(test3)
