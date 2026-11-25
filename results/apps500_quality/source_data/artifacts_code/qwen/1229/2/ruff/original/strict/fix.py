def min_cost_to_make_easy_to_remember(n, m, strings, costs):
    # Initialize the cost to 0
    total_cost = 0

    # Iterate over each position in the strings
    for j in range(m):
        # Create a dictionary to count occurrences of each character at position j
        char_count = {}
        for i in range(n):
            char = strings[i][j]
            if char in char_count:
                char_count[char].append(i)
            else:
                char_count[char] = [i]

        # Iterate over each character and its positions
        for positions in char_count.values():
            if len(positions) > 1:
                # Find the minimum cost to make this character unique at position j
                min_cost = min(costs[i][j] for i in positions)
                total_cost += min_cost

    return total_cost

# Read input
import sys

input = sys.stdin.read
data = input().split()

# Parse input
n = int(data[0])
m = int(data[1])
strings = data[2:2+n]
costs = [list(map(int, data[2+n+2*i:2+n+2*i+m])) for i in range(n)]

# Calculate and print the result
result = min_cost_to_make_easy_to_remember(n, m, strings, costs)
print(result)
