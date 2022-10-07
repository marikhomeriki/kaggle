import collections
from itertools import count


def minion_game(string):

    if string[0] in ['a', 'e', 'i', 'o', 'u']:
        i = string.index(s)
        word1 = string[i:]
    else:
        word2 = string

    x = count_scores(word1)
    print(x)


def count_scores(word):
    score = 0
    for i in range(1, len(word)+1):
        k_words = k_words + word[0:i]
        s_count = word_count(word, k_words)
        kevin += s_count
        k_words = ''

    return score


def word_count(string, word):
    score = 0
    for i in range(len(string)):
        index = string.find(word)
        if index > -1:
            score += 1
            string = string[index+1:]

    return score


def word_count1(string, word):
    count = 0
    start = 0
    while True:
        start = string.find(word, start) + 1
        if start > 0:
            count += 1
        else:
            return count


string = "banana"

print(minion_game(string))
# print(word_count(string, "anana"))
