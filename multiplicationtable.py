def multiplication_table(size):
    columns = []

    for i in range(1, size+1):
        rows = []
        for j in range(1, size+1):
            rows.append(i*j)
        columns.append(rows)

    return columns


size = 3

print(multiplication_table(size))
