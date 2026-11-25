import sys


def solve():
    n = int(input())
    a = list(map(int, input().split()))

    freq = [0] * (n + 1)
    for i in range(n):
        freq[a[i]] += 1

    ans = 1
    cur = 0
    for i in range(1, n + 1):
        if freq[i] == 0:
            return 0
        if freq[i] > 1:
            cur += 1
        else:
            ans *= cur
            cur = 0

    ans *= cur
    print(ans)


if __name__ == "__main__":
    solve()
