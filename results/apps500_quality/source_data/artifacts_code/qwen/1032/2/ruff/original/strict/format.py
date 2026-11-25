from math import factorial


def good_integers(n, p, a):
    a.sort()
    if a[0] >= n - 1:
        return 0, []
    good = [0] * (n + 1)
    good[n] = 1
    for i in range(n - 1, 0, -1):
        good[i] = (
            good[i + 1] * (n - i)
            + sum(good[i + 1 + j] * factorial(j) for j in range(1, min(n - i, p + 1)))
        ) % p
    return sum(good), [i for i in range(1, n + 1) if good[i] > 0]


n, p = map(int, input().split())
a = list(map(int, input().split()))
result = good_integers(n, p, a)
print(result[0])
print(" ".join(map(str, result[1])))
