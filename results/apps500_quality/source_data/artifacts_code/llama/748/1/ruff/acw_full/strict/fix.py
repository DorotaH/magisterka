

def solve():
	n = int(input())
	a = list(map(int, input().split()))

	if n == 3:
		if a[0] == a[1] == a[2]:
			print(-1)
		else:
			print(a[0], a[1], a[2])
	else:
		b = [a[0]]
		for i in range(1, n):
			if a[i] % b[-1] != 0:
				b.append(a[i])
			else:
				b.append(a[i])
				while b[-3] % b[-2] != 0 or b[-2] % b[-1] != 0:
					b.pop()
				if len(b) == 3:
					b.pop()
		if len(b) != n:
			print(-1)
		else:
			for i in range(0, n, 3):
				print(*b[i:i + 3], end=" ")
			print()


if __name__ == "__main__":
	solve()
