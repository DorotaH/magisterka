

def calculate_probability(n, m):
	# Calculate the total number of cards
	total_cards = m * n

	# Calculate the probability of drawing two cards from different decks
	prob_different = ((m - 1) * n) / (m * n)

	# Calculate the probability of drawing the same card after shuffling
	prob_same = 1 / (m * n)

	return (prob_same * prob_different) + (0.5 * (1 - prob_different))


# Read input from standard input
input_str = input().split()
n = int(input_str[0])
m = int(input_str[1])

# Calculate and print the probability
prob = calculate_probability(n, m)
print(format(prob, ".6f"))
