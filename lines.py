def number(lines):
    for i in range(len(lines)):
        lines[i] = (f"{i+1}: {lines[i]}")
    return lines


lines = ["a", "b", "c"]
number(lines)


['1 : a', '2 : b', '3 : c']
['1: a', '2: b', '3: c']
