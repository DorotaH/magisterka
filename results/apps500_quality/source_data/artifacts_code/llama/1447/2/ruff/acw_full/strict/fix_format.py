n, m = map(int, input().split())

# Calculate the total number of cards
total_cards = m * n

# Calculate the number of cards that are identical
identical_cards = m * (n - 1) + 1

# Calculate the probability
probability = (1 - 1 / n) * (1 / n) + (1 - (1 - 1 / n)) * (1 / (1 + n))

print(format(probability, ".10f"))
