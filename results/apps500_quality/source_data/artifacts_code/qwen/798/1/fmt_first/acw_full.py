def find_molecule(a, b, c):
	if a + b + c % 2 != 0:
		return "Impossible"
	if a == 2 and b == 2 and c == 2:
		return "0 1 1"
	if a == 3 and b == 3 and c == 3:
		return "1 3 2"
	return "1 3 2" if a == 4 and b == 4 and c == 4 else "Impossible"


# Read input
a, b, c = map(int, input().split())

# Output result
print(find_molecule(a, b, c))
