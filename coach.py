def coach_answer(message):
    if message == "I am going to work right now!":
        return ""
    if message.endswith("?"):
        return "Silly question, get dressed and go to work!"
    else:
        return "I don't care, get dressed and go to work!"


def coach_answer_enhanced(message):
    if message == "I AM GOING TO WORK RIGHT NOW!":
        return ""
    if message.isupper():
        return "I can feel your motivation!" + coach_answer(message)


message = "Can I eat some pizza?"
message = message.upper()


print(coach_answer_enhanced(message))
