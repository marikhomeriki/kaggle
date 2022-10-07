
def minion_game(string):

    words_a = []
    words_b = []
    k_score = 0
    s_score = 0
    kevin = "Kevin"
    stuart = "Stuart"

    word_a = string[first_vowel(string):]
    word_b = string[first_not_vowel(string):]

    a = all_words_a(word_a)
    b = all_words_b(word_b)

    for word in a:
        words_a.append(get_words(word))

    for word in b:
        words_b.append(get_words(word))

    for i in range(len(words_b)):
        for j in range(len(words_b[i])):
            s_score = s_score + score_count(string, words_b[i][j])

    for i in range(len(words_a)):
        for j in range(len(words_a[i])):
            k_score = k_score + score_count(string, words_a[i][j])

    if k_score > s_score:
        return f"{kevin} {k_score}"
    else:
        return f"{stuart} {s_score}"


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
    score = 0
    for i in range(1, len(word)+1):
        sub_words = sub_words + word[0:i]
        b_words.append(sub_words)
        sub_words = ''
    return b_words


def all_words_b(word):
    words_b = set()
    for s in word:
        if s not in ['A', 'E', 'I', 'O', 'U']:
            words_b.add(word[word.find(s):])
    return words_b


def all_words_a(word):
    words_a = set()
    for s in word:
        if s in ['A', 'E', 'I', 'O', 'U']:
            words_a.add(word[word.find(s):])
    return words_a


def first_vowel(s):
    for index, char in enumerate(s):
        if char in 'AEIOU':
            return index


def first_not_vowel(s):
    for index, char in enumerate(s):
        if char not in 'AEIOU':
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


word = "BANANA"
print(minion_game(word))
