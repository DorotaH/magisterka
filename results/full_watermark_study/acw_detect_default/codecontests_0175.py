T = int(input())
for _ in range(T):
	n = int(input())
	B = [int(i) for i in input().split()]
	m = n * (1 + n) // 2
	if sum(B) % m != 0:
		print("NO")
	else:
		A = sum(B) // m

		ans = [(i + A - j) / n for i, j in zip(B, [B[0]] + B[1:])]
		if any(int(x) != x or 0 >= x for x in ans):
			print("NO")
		else:
			print("YES")
			print(" ".join(str(int(x)) for x in ans[:-1] + [ans[-1]]))
