n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Convert b to a set for faster lookup
b_set = set(b)

# Sort the prices of the questions in descending order
a.sort(reverse=True)

# Initialize the current player's points to 0
current_points = 0

total_points = sum(
	min(a[i], current_points) if i + 1 in b_set else a[i] for i in range(n)
)
# Print the total points
print(total_points)
