import sys
from collections import defaultdict


def easy_to_remember(n, m, strings, costs):
	# Create a 2D array to store the frequency of each character at each position
	freq = [[0] * m for _ in range(26)]

	# Count the frequency of each character at each position
	for string in strings:
		for j, char in enumerate(string):
			freq[ord(char) - ord("a")][j] += 1

	# Initialize the answer
	answer = 0

	# Check if it's possible to make the multiset easy to remember
	for i in range(n):
		for j in range(m):
			# If the frequency of the character at this position is more than 1
			if freq[ord(strings[i][j]) - ord("a")][j] > 1:
				# Try to change the character at this position to all possible characters
				for k in range(26):
					if k != ord(strings[i][j] - ord("a")) and all(freq[k][j] == 1):
						answer = min(answer, costs[i][j])
						# If changing the character at this position to this character makes the multiset easy to remember
						if freq[k][j] == 1:
							# Decrement the frequency of all characters at this position
							for char in range(26):
								freq[char][j] -= 1
							# Decrement the answer by the cost of changing the character
							answer -= costs[i][j]
							# Break the loop
							break
						# If changing the character at this position to this character doesn't make the multiset easy to remember
						else:
							# Decrement the frequency of the current character at this position
							freq[ord(strings[i][j] - ord("a"))][j] -= 1

	# Return the answer
	return answer


# Read the input
n, m = map(int, input().split())
strings = []
costs = []
for _ in range(n):
	strings.append(input())
	costs.append(list(map(int, input().split())))

# Print the answer
print(easy_to_remember(n, m, strings, costs))
