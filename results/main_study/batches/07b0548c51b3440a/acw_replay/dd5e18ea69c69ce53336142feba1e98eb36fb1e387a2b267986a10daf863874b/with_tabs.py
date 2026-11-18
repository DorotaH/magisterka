from heapq import heappush, heappop

N = int(input())
A = [int(a) for a in input().split()]
for i in range(N):
	if 0 > A[i]:
		k = i
		break
A = [0] + [0 if i < k else A[i] for i in range(N) if i != k]

ans = A.pop()
H = []
while 2 < N:
	N //= 2
	for _ in range(N):
		heappush(H, A.pop())
	ans += heappop(H)

print(ans)
