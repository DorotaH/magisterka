def determine_winner(n):
    return ("white", 1, 2) if n % 2 == 0 else ("black", 0, 0)


# Read input
n = int(input().strip())

# Determine the winner and the first move
winner, r, c = determine_winner(n)

# Print the result
print(winner)
if winner == "white":
    print(r, c)
