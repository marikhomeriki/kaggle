from curses.ascii import isalpha


def wave(people):
    result = []
    word = ''
    size = len(people)
    for i in range(size):
        c = people[i].upper()
        word = word + c + people[i+1:]
        if people[i] != " ":
            result.append(word)
        word = word[:i+1].lower()
    return result


people = "Two words"
print(people[0:0])


def wave1(people):
    return [people[0:i] + people[i].upper() + people[i+1:] for i in range(len(people)) if people[i].isalpha()]


print(wave1(people))
