def restore_sequence(b):
	n = len(b)
	a = [0] * n
	a[0] = b[0]
	carry = 0
	for i in range(1, n):
		while True:
			a[i] = a[i - 1] + 1
			if sum(int(digit) for digit in str(a[i])) == b[i]:
				break
	return a


# Read input
n = int(input())
b = [int(input()) for _ in range(n)]

# Restore sequence
a = restore_sequence(b)

# Print the result
for num in a:
	print(num)
