import  sys
import  math

def  calculate_probability(n, m):
    # Calculate the total number of cards
    total_cards = m * n

    # Calculate the probability of drawing two cards from different decks
    prob_different = (n * (m - 1)) / (m * n)

    # Calculate the probability of drawing the same card after shuffling
    prob_same = 1 / (m * n)

    # Calculate the probability of the trick being successful
    prob_successful = (prob_different * prob_same) + ((1 - prob_different) * 0.5)

    return  prob_successful


# Read input from standard input
input_str = input().split()
n = int(input_str[0])
m = int(input_str[1])

# Calculate and print the probability
prob = calculate_probability(n, m)
print(format(prob, ".6f"))