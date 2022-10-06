def spin_words(sentence):
    result = ""
    arr = sentence.split()
    for i in range(len(arr)):
        if len(arr[i]) >= 5:
            reverse = arr[i][::-1]
            arr[i] = reverse
    result = " ".join(arr)
    return result


sentence = "Hey fellow warriors"
sentence1 = "This is a test"
sentence2 = "This is another test"
sentence3 = "warriors"
sentence4 = 'letters more or reversed Write when be five the same words or'

print(spin_words(sentence))
print(spin_words(sentence1))
print(spin_words(sentence2))
print(spin_words(sentence3))
print(spin_words(sentence4))
