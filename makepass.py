def make_password(phrase):
    words = phrase.split()
    password = ''
    for word in words:
        if word[0] in ("i", "o", "s", "I", "O", "S"):
            print("test")
            password = password + word[0].lower()
        else:
            password = password + word[0]

    return password.replace("o", "0").replace("i", "1").replace("s", "5")


phrase = "Give me liberty or give me death"
phrase2 = "Keep Calm and Carry On"

print(make_password(phrase2))
