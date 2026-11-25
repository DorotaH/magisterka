import math


def solve():
    n = int(input())
    boxes = []
    for _ in range(n):
        k, a = map(int, input().split())
        boxes.append((k, a))

    boxes.sort(key=lambda x: x[0])

    max_k = boxes[0][0]
    for k, a in boxes:
        if (2 ** (k + 1)) < (2 ** max_k):
            max_k = max(max_k, k)

    print(math.floor(max_k + 1))


solve()
