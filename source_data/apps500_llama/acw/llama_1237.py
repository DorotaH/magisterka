from collections import deque
import sys


def solve():
	n = int(input())
	a = list(map(int, input().split()))
	k = int(input())
	b = list(map(int, input().split()))
	a_idx = {val: i for i, val in enumerate(a)}
	b_idx = {val: i for i, val in enumerate(b)}

	if any(b[j] <= a[i] for i, j in zip(a_idx.values(), b_idx.values())):
		print('NO')
		return

	eaten = {i: False for i in range(n)}
	eaten[0] = True
	ans = []
	p = deque(list(range(n)))

	for i in range(n):
		if eaten[i]:
			continue
		for j in range(i + 1, n):
			if eaten[j]:
				continue
			if a[j] > a[i]:
				eaten[i] = True
				eaten[j] = True
				if a[j] > a[i]:
					a[a_idx[a[i]]] += a[j]
					a[a_idx[a[j]]] = a[i]
					ans.append(f'{a_idx[a[i]]} L')
				else:
					a[a_idx[a[i]]] += a[i]
					a[a_idx[a[j]]] = a[j]
					ans.append(f'{a_idx[a[i]]} R')
				p = deque([i if eaten[i] else j for i in range(n)])
				break
		if eaten[i]:
			continue
		for j in range(i - 1, -1, -1):
			if eaten[j]:
				continue
			if a[j] > a[i]:
				eaten[i] = True
				eaten[j] = True
				if a[j] > a[i]:
					a[a_idx[a[i]]] += a[j]
					a[a_idx[a[j]]] = a[i]
					ans.append(f'{a_idx[a[i]]} L')
				else:
					a[a_idx[a[i]]] += a[i]
					a[a_idx[a[j]]] = a[j]
					ans.append(f'{a_idx[a[i]]} R')
				p = deque([i if eaten[i] else j for i in range(n)])
				break

	if not ans:
		print('NO')
	else:
		print('YES')
		for i in range(len(ans)):
			print(ans[i])
			p = deque([i + 1 if eaten[i] else i for i in range(n)])


if __name__ == '__main__':
	solve()
