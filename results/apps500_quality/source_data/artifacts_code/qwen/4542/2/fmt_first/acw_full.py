import sys


def min_stones_to_place(S):
	# Find the longest segment of consecutive stones of the same color
	max_same_color_segment = 0
	current_segment = 1

	for i in range(1, len(S)):
		if S[i] == S[i - 1]:
			current_segment += 1
		else:
			max_same_color_segment = max(max_same_color_segment, current_segment)
			current_segment = 1
	max_same_color_segment = max(max_same_color_segment, current_segment)

	# The minimum number of stones needed to make all stones the same color
	return len(S) - max_same_color_segment


# Read input from standard input
S = sys.stdin.read().strip()

# Output the result
print(min_stones_to_place(S))
