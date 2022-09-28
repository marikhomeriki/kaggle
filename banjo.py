def are_you_playing_banjo(name):
    first_char = name.lower()[0]
    if first_char == 'r':
        name = name + " plays banjo"
    else:
        name = name + " does not play banjo"

    return name


name = 'Mari'
print(are_you_playing_banjo(name))
