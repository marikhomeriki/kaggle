import collections
from ctypes import resize


def paint_letterboxes1(start, finish):
    freq_letters = {}
    st_start = ''

    box_range = (finish - start) + 1
    for i in range(box_range):
        st_start = st_start + str(start)
        start = start + 1

    to_array = [char for char in st_start]

    to_array = sorted(to_array)
    freq_letters = collections.Counter(to_array)

    for i in range(10):
        i = str(i)
        if st_start.find(i) == -1:
            freq_letters[i] = 0


start = 125
finish = 132


def paint_letterboxes(start, finish):
    result = [0] * 10
    for n in range(start, finish+1):
        for i in str(n):
            result[int(i)] += 1
    return result


def paint_letterboxes2(s, f):
    a = collections.Counter("".join(map(str, range(s, f+1))))
    return [a[x] for x in "0123456789"]


s = 125
f = 132
print(paint_letterboxes(start, finish))
print(paint_letterboxes2(s, f))
