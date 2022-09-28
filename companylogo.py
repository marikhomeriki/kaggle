import collections


def create_dict(string):
    letters = {}
    length = len(string)
    for i in range(length):
        ltr = string[i]
        if letters.get(ltr) == None:
            letters[ltr] = 1
        else:
            val = letters.get(ltr) + 1
            letters[ltr] = val
    return letters


string = "aaabbbcccde"

d = create_dict(string)
str = sorted(string)
print(str)
print(create_dict(string))
# print(a[l-1][0] + ' ' + str(a[l-1][1]))
# print(a[l-2][0] + ' ' + str(a[l-2][1]))
# print(a[l-3][0] + ' ' + str(a[l-3][1]))

s_counter = collections.Counter(str).most_common()
print(s_counter)
