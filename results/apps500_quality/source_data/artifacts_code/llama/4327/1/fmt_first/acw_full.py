A, P = map(int, input().split())
max_pies = 0
for i in range(1 + A):
	if (A - i) * 3 >= P:
		pies_from_apples = (A - i) // 3
		pies_from_pieces = P // 2
		max_pies = max(max_pies, pies_from_pieces + pies_from_apples)
print(max_pies)
