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


def blackjack_hand_greater_than(hand_1, hand_2):
    total_1 = hand_total(hand_1)
    total_2 = hand_total(hand_2)


hand = 'A', 'A', 'J', '6'
score = hand_total(hand)
print(score)
