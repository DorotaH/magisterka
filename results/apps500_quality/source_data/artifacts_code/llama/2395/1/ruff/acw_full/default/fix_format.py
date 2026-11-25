def find_period(s):
    n = len(s)
    return next((k for k in range(1, 1 + n) if (n // k) * s[:k] == s), n)


def solve():
    t = int(input())
    for _ in range(t):
        s = input()
        k = find_period(s)
        result = s * (2 * len(s) // k)
        print(result)


solve()
