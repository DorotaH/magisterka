def initial_position(n, x):
	if n % 2 == 0:
		return x
	if x == 0:
		return 1
	elif x == 1:
		return 0
	else:
		return 2


# Read input
n = int(input().strip())
x = int(input().strip())

# Output the result
print(initial_position(n, x))
