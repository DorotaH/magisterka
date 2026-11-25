from collections import deque

n = int(input())
a = list(map(int, input().split()))

d = {}
queue = deque([a[0]])
for i in range(1, n):
    queue.append(a[i])
    d[a[i]] = 0

for i in range(1, n):
    if a[i - 1] < a[i]:
        d[a[i]] = d[a[i - 1] + 1] + 1
    elif a[i - 1] > a[i]:
        d[a[i]] = d[a[i - 1] - 1] + 1

print(sum(abs(i - (1 + n - i)) for i in range(1 + n)) - min(d.values()))
