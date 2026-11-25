from sys import stdin, stdout

# Read input
n = int(stdin.read().strip())

# Initialize count of xorangles
count = 0

# Iterate over all possible values of a, b, c
for a in range(1, 1 + n):
	for b in range(a, 1 + n):
		for c in range(b, 1 + n):
			# Check if the sides form a non-degenerate triangle and their xor-sum is zero
			if a + b > c and a ^ b ^ c == 0:
				count += 1

# Write output
stdout.write("\n" + str(count))
