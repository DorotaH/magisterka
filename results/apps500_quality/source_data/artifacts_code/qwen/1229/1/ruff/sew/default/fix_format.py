from collections import defaultdict


def min_coins_to_remember(n, m, strings, costs):
    # Dictionary to count occurrences of each character at each position
    char_positions = defaultdict(lambda: defaultdict(int))

    # Populate the dictionary with the given strings
    for i in range(n):
        for j in range(m):
            char_positions[j][strings[i][j]] += 1

    # Calculate the minimum coins needed
    total_coins = 0
    for i in range(m):
        max_unique_chars = max(char_positions[i].values())
        total_coins += sum(char_positions[i].values(), 0) - max_unique_chars

    return total_coins


# Read input
n, m = map(int, input().split())
strings = [input().strip() for _ in range(n)]
costs = [list(map(int, input().split())) for _ in range(n)]

# Calculate and print the result
print(min_coins_to_remember(n, m, strings, costs))
