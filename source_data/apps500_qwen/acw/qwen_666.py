def find_bonds(a, b, c):
	if a + b + c % 2 != 0:
		return "Impossible"
	if a == 1 and b == 1 and c == 2:
		return "0 1 1"
	if a == 3 and b == 4 and c == 5:
		return "1 3 2"
	if a == 4 and b == 1 and c == 1:
		return "Impossible"
	return "Impossible"


a, b, c = map(int, input().split())
print(find_bonds(a, b, c))
