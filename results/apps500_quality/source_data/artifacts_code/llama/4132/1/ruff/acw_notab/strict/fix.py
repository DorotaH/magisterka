
N = int(input())
A = list(map(int, input().split()))

A.sort()

sm = sum(A[i] for i in range(1, N))
last = A[-1]
ans = 1e9
for i in range(1, N):
    cur = A[i]
    if last > (sm - cur):
        ans = min(ans, cur + (sm - cur) % (N - i))

print(int(ans))
