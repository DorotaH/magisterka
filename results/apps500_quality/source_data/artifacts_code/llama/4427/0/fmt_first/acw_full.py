# Read input from standard input
r, D, x_2000 = map(int, input().split())

# Calculate and print x_{2001}, ..., x_{2010}
for _ in range(10):
	x_next = x_2000 * r - D
	print(x_next)
	x_2000 = x_next
