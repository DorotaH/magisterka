
N = int(input())
A = list(map(int, input().split()))

A.sort()

sm = 0
for i in range(1, N):
    sm += A[i]

last = A[-1]
ans = 1e9
for i in range(1, N):
    cur = A[i]
    if (sm - cur) < last:
        ans = min(ans, cur + (sm - cur) % (N - i))

print(int(ans))
