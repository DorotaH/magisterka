n, m = list(map(int, input().split()))

field = [input() for _ in range(n)]
ans = 0
for i in range(n - 1):
	for j in range(m - 1):
		t = set()
		t.add(field[i][j])
		t.add(field[i + 1][1 + j])
		t.add(field[i + 1][j])
		t.add(field[i][1 + j])

		if t == set("face"):
			ans += 1
print(ans)
