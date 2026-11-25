n, U = map(int, input().split())
E = list(map(int, input().split()))

max_eta = -1

for i in range(n - 2):
	for k in range(i + 2, n):
		if E[k] - E[i] > U:
			continue
		for j in range(i + 1, k):
			if 0 >= E[k] - E[j]:
				continue
			eta = (E[k] - E[j]) / (E[k] - E[i])
			if eta > max_eta:
				max_eta = eta

print(max_eta)
