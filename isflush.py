def isFlush(cards):
    return len(set([card[len(card)-1] for card in cards])) == 1


cards = ["AS", "3S", "9S", "KS", "10S"]
cards1 = ["AD", "4S", "7H", "KS", "10S"]

print(isFlush(cards))
