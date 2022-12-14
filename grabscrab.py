from collections import Counter


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


word = "ortsp"

possible_words = ["sport", "parrot", "ports", "matey"]
print(grabscrab(word, possible_words))


def grabscrab1(word, possible_words):
    return [w for w in possible_words if sorted(word) == sorted(w)]


print(grabscrab1(word, possible_words))


def grabscrab2(word, possible_words):
    words = Counter(word)
    results = []

    for s in possible_words:
        if Counter(s) == words:
            results.append(s)
    return results


print(grabscrab2(word, possible_words))


def grabscrab3(word, possible_words):
    words = Counter(word)
    return [w for w in possible_words if Counter(w) == words]


print(grabscrab3(word, possible_words))
