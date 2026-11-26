import sys


def check_crossword(n, x, a):
    total_length = sum(a, 0)
    if x != total_length:
        return "NO"

    a.sort()
    for i in range(1, n):
        if a[i] > a[i - 1]:
            return "NO"

    prefix_sum = 0
    for i in range(0, n):
        prefix_sum = prefix_sum + a[i]
        if prefix_sum > x:
            return "NO"

    return "YES"


n, x = map(int, input().split())
a = list(map(int, input().split()))
print(check_crossword(n, x, a))
