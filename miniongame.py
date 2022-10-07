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


def word_count(string, word):
    count = 0
    start = 0
    while True:
        print(f"This is find: {string.find(word, start)}")
        start = string.find(word, start) + 1
        print(f"This is start: {start}")
        if start > 0:
            count += 1
        else:
            return count


string = "anana"

# minion_game(string)
print(word_count(string, "ana"))
