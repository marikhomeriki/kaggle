def duplicate_count(text):
    freq = {}
    text = text.lower()
    for c in text:
        if freq.get(c) == None:
            freq[c] = 1
        else:
            freq[c] += 1

    print(freq)


text = "aabBcde"
text1 = "aA11"


duplicate_count(text1)
