def maximize_score(a, b):
    # If there are no 'o' cards, return the maximum score if all 'x' cards are arranged in a single block
    if  a == 0:
        return  -1 * b ** 2, 'x' * b

    # If there are no 'x' cards, return the maximum score if all 'o' cards are arranged in a single block
    if  b == 0:
        return  a ** 2, 'o' * a

    # Initialize the result
    max_score, max_deck = -1 * b ** 2, ''
    b_used = a_used = 0

    # Try to use 'x' cards to make the score as big as possible
    for  i in  range(0, b):
        score = -1 * (b - i) ** 2
        deck = 'x' * (b - i) + 'o' * (a - i)

        # If the current score is higher than the max score, update the max score and the deck
        if score > max_score:
            max_score = score
            max_deck = deck
            b_used = b - i
            a_used = a - i

    return  (max_score, max_deck)

a, b=map(int, input().split())
max_score, max_deck=maximize_score(a, b)

print(max_score)
print(max_deck)
