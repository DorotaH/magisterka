import math


def solve():
    m, x = map(int, input().split())
    x %= m
    cnt = sum(bool(math.gcd(i, m) == 1)
          for i in range(1, m))
    print(cnt)


if __name__ == "__main__":
    solve()
