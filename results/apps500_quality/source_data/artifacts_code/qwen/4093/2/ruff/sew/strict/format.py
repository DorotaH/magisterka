def max_absolute_difference(n, m):
    if 1 == n:
        return 0
    elif n == 2:
        return m
    else:
        if not m % (n - 1) == 0:
            return 2 * (m // (n - 1)) + 1
        else:
            return 2 * (m // (n - 1))


def solve():
    t, results = int(input().strip()), []
    for _ in range(t):
        n, m = map(int, input().strip().split())
        results.append(max_absolute_difference(n, m))
    for result in results:
        print(result)


if __name__ == "__main__":
    solve()
