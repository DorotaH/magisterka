import sys


def sum_hamming_distance(a, b):
    n = len(a)
    m = len(b)

    p = 0
    ans = 0

    for i in range(m - n + 1):
        for j in range(n):
            ans += b[i + j] != a[j]
        p += ans
        ans = 0

    return p


a, b = input().strip(), input().strip()

print(sum_hamming_distance(a, b))
