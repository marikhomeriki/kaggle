import collections
from itertools import count


def minion_game(string):
    kevin = 0
    word = ''
    k_words = ""
    for s in string:
        if s in ['a', 'e', 'i', 'o', 'u']:
            i = string.index(s)
            word = string[i:]

    for i in range(len(word)+1):
        k_words = k_words + word[0:i]

        print(k_words)
        k_words = ''


def word_count1(string, word):
    count = 0
    start = 0
    while True:
        start = string.find(word, start) + 1
        if start > 0:
            count += 1
        else:
            return count


def word_count(string, word):
    score = 0
    for i in range(len(string)):
        index = string.find(word)
        if index > -1:
            score += 1
            string = string[index+1:]

    return score


string = "ananana"

# minion_game(string)
word_count(string, "ana")
