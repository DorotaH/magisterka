def maximize_score(a, b):
    # If there are no 'o' cards, return the maximum score if all 'x' cards are arranged in a single block
    if a == 0:
        return b**2 * -1, "x" * b

    # If there are no 'x' cards, return the maximum score if all 'o' cards are arranged in a single block
    if b == 0:
        return a**2, a * "o"

    # Initialize the result
    max_score = b**2 * -1
    max_deck = ""
    b_used = 0
    a_used = 0

    # Try to use 'x' cards to make the score as big as possible
    for i in range(b):
        score = (b - i) ** 2 * -1
        deck = (b - i) * "x" + (a - i) * "o"

        # If the current score is higher than the max score, update the max score and the deck
        if score > max_score:
            max_score = score
            max_deck = deck
            b_used = b - i
            a_used = a - i

    return max_score, max_deck


a, b = map(int, input().split())
max_score, max_deck = maximize_score(a, b)

print(max_score)
print(max_deck)
