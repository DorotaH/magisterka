s = input()

# Calculate the minimum difference between X and 753
min_diff = float('inf')
for i in range(len(s) - 2):
	X = int(s[i:i + 3])
	diff = abs(X - 753)
	min_diff = min(min_diff, diff)

print(min_diff)
