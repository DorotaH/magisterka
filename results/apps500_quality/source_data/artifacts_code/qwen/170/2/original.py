def card_war(n, k1, cards1, k2, cards2):
    fights = 0
    while k1 > 0 and k2 > 0:
        card1 = cards1.pop(0)
        card2 = cards2.pop(0)
        fights += 1
        if card1 > card2:
            cards1.extend([card2, card1])
        elif card2 > card1:
            cards2.extend([card1, card2])
        else:
            # If the cards are equal, the game does not end
            return -1
    return fights, 1 if k1 > 0 else 2

# Read input
n = int(input())
k1 = int(input())
cards1 = list(map(int, input().split()))
k2 = int(input())
cards2 = list(map(int, input().split()))

# Output the result
result = card_war(n, k1, cards1, k2, cards2)
print(result[0], result[1])
