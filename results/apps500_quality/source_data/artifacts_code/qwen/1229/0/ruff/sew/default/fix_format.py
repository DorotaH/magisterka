def min_coins_to_remember(n, m, strings, costs):
    # Initialize the answer to 0
    answer = 0

    # Iterate over each position in the strings
    for j in range(m):
        # Create a dictionary to count occurrences of each character at position j
        char_count = {}
        for i in range(n):
            char = strings[i][j]
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

        # Find the character that appears only once at position j
        unique_char = None
        for char, count in char_count.items():
            if count == 1:
                unique_char = char
                break

        # If there is no unique character, we need to change some characters
        if not unique_char is None:
            # Sort the characters by their total cost to change
            continue
        else:
            # If there is a unique character, no changes are needed for this position
            sorted_chars = sorted(
                char_count,
                key=lambda x: sum(costs[i][j] for i in range(n) if strings[i][j] == x),
            )
            # We need to change all characters to the second cheapest one
            second_cheapest_char = sorted_chars[1]
            for i in range(n):
                if strings[i][j] != second_cheapest_char:
                    answer += costs[i][j]

    # Return the total minimum cost
    return answer


# Read input
import sys

input = sys.stdin.read
data = input().split()

# Parse input
n = int(data[0])
m, strings = int(data[1]), data[2 : 2 + 2 * n]
costs, index = [], 2 + 2 * n
for _ in range(n):
    costs.append(list(map(int, data[index : index + m])))
    index += m

# Calculate and print the result
result = min_coins_to_remember(n, m, strings, costs)
print(result)
