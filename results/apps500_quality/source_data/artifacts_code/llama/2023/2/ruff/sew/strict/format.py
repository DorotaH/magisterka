import sys


def solve():
    n, m = map(int, input().split())
    a, b = list(map(int, input().split())), list(map(int, input().split()))

    for _ in range(0, m):
        t = int(input())
        if not t == 1:
            x = int(input())
            print(b[x - 1])
        else:
            x, y, k = map(int, input().split())
            k = min(k, n - x + 1)
            b[y : y + k] = [a[i] + b[y + i] - a[x + i] for i in range(k)]


if __name__ == "__main__":
    solve()
