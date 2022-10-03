def even_chars(st):
    result = []
    if len(st) == 1 or len(st) > 1000:
        return "Invalid String"

    for i in range(len(st)):
        if i % 2 == 1:
            result.append(st[i])
    return result


st = "abcdefghijklm"
st1 = "a"

print(even_chars(st))
