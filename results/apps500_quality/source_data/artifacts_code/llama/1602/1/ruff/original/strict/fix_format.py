import sys

input = sys.stdin.readline


def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = [0] * n
    for i in range(n):
        ans[i] = a[i]

    for i in range(1, n):
        x = a[i]
        for j in range(i):
            x = x | a[j]
        ans[i] = x - a[i]

    print(*sorted(ans, reverse=True))


t = 1
for _ in range(t):
    solve()
