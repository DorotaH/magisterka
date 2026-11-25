import sys

n, d = map(int, input().split())
t = list(map(int, input().split()))

total_time = 0
jokes = 0

for i in range(n):
    if t[i] + total_time + 10 > d:
        print(-1)
        sys.exit()
    total_time += t[i]
    jokes += (d - total_time - 10 - t[i]) // 5
    total_time += t[i] + 10

print(jokes)
