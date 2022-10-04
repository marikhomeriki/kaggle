def grabscrab(word, possible_words):

    count = 0
    result = []

    for i in range(len(possible_words)):
        for c in word:
            if len(word) != len(possible_words[i]):
                continue
            if word.count(c) == possible_words[i].count(c):
                count += 1
                if count == len(possible_words[i]):
                    count = 0
                    result.append(possible_words[i])

    return result


word = "ilfe"

possible_words = ["make", ]
print(grabscrab(word, possible_words))
