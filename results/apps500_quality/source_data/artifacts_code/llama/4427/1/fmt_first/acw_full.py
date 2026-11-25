# Read input from standard input
r, D, x_2000 = map(int, input().split())

# Check if input constraints are satisfied
assert 2 <= r <= 5, "r should be between 2 and 5"
assert 1 <= D <= 100, "D should be between 1 and 100"
assert 1 <= x_2000 <= 200, "x_2000 should be between 1 and 200"
assert x_2000 > D, "D should be less than x_2000"

# Calculate and print x_{2001}, ..., x_{2010}
for _ in range(10):
	x_next = x_2000 * r - D
	print(x_next)
	x_2000 = x_next
