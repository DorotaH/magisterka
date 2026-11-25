import math


def  solve():
    n, boxes = int(input()), []
    for  _ in  range(n):
        k, a = map(int, input().split())
        boxes.append((k, a))

    boxes.sort(key=lambda x: x[0])

    max_k = boxes[0][0]
    for  k, a in  boxes:
        if (pow(2, (k + 1)))<(pow(2, max_k)):
            max_k = max(max_k, k)

    print(math.floor(1 + max_k))

solve()
