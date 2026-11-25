n, m = map(int, input().split())

# Calculate the probability of pulling a card from the same deck
prob_same_deck = (m - 1) / m

# Calculate the probability of pulling a card from a different deck
prob_different_deck = 1 / m

# Calculate the probability of pulling the same card twice
prob_success_same_deck = 1

# Calculate the probability of pulling the same card twice when the cards are from different decks
prob_success_different_deck = 1 / (2 * n)

# Calculate the overall probability of success
probability = prob_same_deck * prob_success_same_deck + prob_success_different_deck * prob_different_deck

print(probability)
