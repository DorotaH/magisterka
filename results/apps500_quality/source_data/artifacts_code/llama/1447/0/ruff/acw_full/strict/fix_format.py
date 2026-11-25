from math import comb

n, m = map(int, input().split())
total_cards = m * n

# Calculate the probability of choosing a pair of cards with the same value
same_value_probability = (comb(n, 2) * (n - 1) * m) / (total_cards * (total_cards - 1))

# Calculate the probability of choosing a pair of cards with different values
different_values_probability = 1 - same_value_probability

# Calculate the probability of the trick being successful if the cards have different values
success_probability_different_values = 1 / 2

# Calculate the total probability of the trick being successful
total_success_probability = same_value_probability + (
    different_values_probability * success_probability_different_values
)

print(f"{total_success_probability:.6f}")
