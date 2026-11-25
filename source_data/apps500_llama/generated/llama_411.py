import sys
import math

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

boxes = [[] for _ in range(n + 1)]
for i in range(n):
    boxes[a[i]].append(i)

ans = 0
for i in range(1, n + 1):
    ans += len(boxes[i])
    for j in range(i + 1, n + 1):
        if boxes[i]:
            for k in boxes[j]:
                boxes[a[k]].remove(k)
                boxes[i].append(k)

print(ans)
