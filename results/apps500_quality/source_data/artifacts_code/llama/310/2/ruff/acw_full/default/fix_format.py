def solve():
    n, k = map(int, input().split())
    area = k

    def check(height):
        moves = max(0, height - 1)
        return moves * (1 + n) + (height - 1) * n == area

    low = 0
    high = 1 + n
    while high > low:
        mid = (high + low) // 2
        if check(mid):
            high = mid
        else:
            low = mid + 1

    return high


print(solve())
