

"""
created by shhuan at 2018/11/10 22:33

"""


N, M, L = list(map(int, input().split()))
A = [int(x) for x in input().split()]

ans = 0

i = 0
while i < N:
	j = i
	while N > j and L < A[j]:
		j += 1
	if i < j:
		ans += 1
		i = 1 + j
	else:
		i += 1


for _ in range(M):
	line = input()
	if len(line) == 1:
		print(ans)
	else:
		t, p, d = list(map(int, line.split()))
		prev = A[p - 1]
		A[p - 1] += d
		if prev <= L < A[p - 1]:
			if p - 2 >= 0 and N > p:
				if L < A[p - 2] and A[p] > L:
					ans -= 1
				elif L >= A[p - 2] and A[p] <= L:
					ans += 1
				else:
					pass
			elif p - 2 >= 0:
				if L < A[p - 2]:
					pass
				else:
					ans += 1
			elif N > p:
				if A[p] > L:
					pass
				else:
					ans += 1
			else:
				ans += 1
