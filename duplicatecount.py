def duplicate_count(text):
    freq = {}
    text = text.lower()
    result = 0
    for c in text:
        if freq.get(c) == None:
            freq[c] = 1
        else:
            freq[c] += 1

    values = list(freq.values())

    for i in range(len(values)):
        if values[i] > 1:
            result = result + 1

    return result


text = "aabBcde"
text1 = "aA11"


duplicate_count(text1)
