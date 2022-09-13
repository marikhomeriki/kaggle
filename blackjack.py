def hand_total(hand):
    total = 0
    aces = 0

    for card in hand:
        if card in ('J', 'K', 'Q'):
            total += 10
        elif card == 'A':
            aces += 1
        else:
            total += int(card)

    total += aces

    while total + 10 <= 21 and aces > 0:
        print(total)
        total += 10
        aces += -1
    return total


hand = 'A', 'A', 'J', '6'
score = hand_total(hand)
print(score)
