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
