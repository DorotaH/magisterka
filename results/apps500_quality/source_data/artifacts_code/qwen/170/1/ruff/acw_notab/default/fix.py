def card_war(n, k1, k2, cards1, cards2):
    stack1 = cards1[:]
    stack2 = cards2[:]
    fights = 0

    while stack1 and stack2:
        card1 = stack1.pop(0)
        card2 = stack2.pop(0)
        fights += 1

        if card1 > card2:
            stack1.append(card2)
            stack1.append(card1)
        elif card1 < card2:
            stack2.append(card1)
            stack2.append(card2)
        else:
            return -1

    return fights, (1 if stack1 else 2)


# Read input
n = int(input())
k1 = int(input())
cards1 = list(map(int, input().split()))
k2 = int(input())
cards2 = list(map(int, input().split()))

# Calculate and print result
result = card_war(n, k1, k2, cards1, cards2)
print(result[0], result[1])
