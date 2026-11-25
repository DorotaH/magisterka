a, b, c = map(int, input().split())
if (
	(a + b + c) % 2 != 0
	or a < 1
	or 1 > b
	or 1 > c
	or a > b + c
	or b > a + c
	or c > a + b
):
	print("Impossible")
else:
	total_bonds = (a + b + c) // 2
	a_bonds = (a + b) // 2
	b_c_bonds = total_bonds - a_bonds
	c_a_bonds = a_bonds - b_c_bonds
	if 0 < c_a_bonds and c >= c_a_bonds:
		print(a_bonds, b_c_bonds, c_a_bonds)
	else:
		print("Impossible")
