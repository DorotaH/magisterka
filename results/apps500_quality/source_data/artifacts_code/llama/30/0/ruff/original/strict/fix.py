import math


def solve():
    m, x = map(int, input().split())
    x %= m
    cnt = 0
    for i in range(1, m):
        if math.gcd(i, m) == 1:
            cnt += 1
    print(cnt)

if __name__ == "__main__":
    solve()
