import math


def solve():
    n, k = map(int, input().split())
    area = k

    def check(height):
        moves = max(0, height - 1)
        return (moves * (n + 1)) + ((height - 1) * n) == area

    low, high = 0, n + 1
    while low < high:
        mid=(high + low)//2
        if check(mid):
            high = mid
        else:
            low = mid + 1

    return high


print(solve())