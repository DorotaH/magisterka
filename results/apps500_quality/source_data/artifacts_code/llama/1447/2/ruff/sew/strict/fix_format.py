n, m = map(int, input().split())

# Calculate the total number of cards
total_cards = n * m

# Calculate the number of cards that are identical
identical_cards = 1 + m * (n - 1)

# Calculate the probability
probability = ((1 / n) * (1 - 1 / n)) + ((1 - (1 - 1 / n)) * (1 / (n + 1)))

print(format(probability, ".10f"))
