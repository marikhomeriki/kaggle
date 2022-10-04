def duplicate_encode(word):
    st = ""
    word = word.lower()
    letters = {}

    for letter in word:
        if letter not in letters:
            letters[letter] = 0
        letters[letter] += 1

    for c in word:
        if letters.get(c) > 1:
            st = st + ')'
        else:
            st = st + '('

    return st


word = "Success"

duplicate_encode(word)
