import sys

input = sys.stdin.readline

n, a = int(input()), list(map(int, input().split()))

boxes = []
for _ in range(n + 1):
    boxes.append([])
for  i in  range(n):
    boxes[a[i]].append(i)

ans = 0
for  i in  range(1, 1 + n):
    ans += len(boxes[i])
    for  j in  range(i + 1, n + 1):
        if boxes[i]:
            for  k in  boxes[j]:
                boxes[a[k]].remove(k)
                boxes[i].append(k)

print(ans)
