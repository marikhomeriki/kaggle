
def minion_game(string):

    word_a = string[first_vowel(string):]
    word_b = string[first_not_vowel(string):]

    a = all_words_a(word_a)
    b = all_words_b(word_b)


word = "banana"


def score_count(string, word):
    score = 0
    for i in range(len(string)):
        index = string.find(word)
        if index > -1:
            score += 1
            string = string[index+1:]

    return score


def get_words(word):
    b_words = []
    sub_words = ''
    for i in range(1, len(word)+1):
        sub_words = sub_words + word[0:i]
        b_words.append(sub_words)
        sub_words = ''
    return b_words


print(get_words(word))


def all_words_b(word):
    words_b = set()
    for s in word:
        if s not in ['a', 'e', 'i', 'o', 'u']:
            words_b.add(word[word.find(s):])
    return words_b


def all_words_a(word):
    words_a = set()
    for s in word:
        if s in ['a', 'e', 'i', 'o', 'u']:
            words_a.add(word[word.find(s):])
    return words_a


def first_vowel(s):
    for index, char in enumerate(s):
        if char in 'aeiou':
            return index


def first_not_vowel(s):
    for index, char in enumerate(s):
        if char not in 'aeiou':
            return index


def word_count1(string, word):
    count = 0
    start = 0
    while True:
        start = string.find(word, start) + 1
        if start > 0:
            count += 1
        else:
            return count


print(minion_game(word))
