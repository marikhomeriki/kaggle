def split_the_bill(x):
    keys = list(x.keys())
    values = list(x.values())

    sum_val = 0
    for i in range(len(values)):
        sum_val = sum_val + values[i]

    print(sum_val)
    for i in range(len(values)):
        x[keys[i]] = round(values[i] - sum_val/len(values), 2)
    return x


group = {
    "A": 23.0,
    "B": 19.0,
    "C": 34.0
}

print(split_the_bill(group))
