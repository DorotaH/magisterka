import sys


def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    for _ in range(m):
        t = int(input())
        if t == 1:
            x, y, k = map(int, input().split())
            k = min(k, n - x + 1)
            b[y:y + k] = [a[i] + b[i + y] - a[i + x] for i in range(k)]
        else:
            x = int(input())
            print(b[x - 1])


if __name__ == "__main__":
    solve()
