def wave(people):
    result = []
    word = ''
    size = len(people)
    for i in range(size):
        c = people[i].upper()
        word = word + c + people[i+1:]
        if people[i] != " ":
            result.append(word)
        word = word[0:i+1].lower()
    print(result)


people = "Two words"

wave(people)
