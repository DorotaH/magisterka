t = int(input())


def solve(x, n):
    if n % 4 == 0:
        return x
    if n % 4 == 2:
        return 1 + x if x % 2 == 0 else x - 1
    if n % 4 == 1:
        return x - n if x % 2 == 0 else x + n
    if x % 2 == 0:
        return x + n + 1
    return x - n - 1


for _ in range(t):
    x, n = map(int, input().split())

    print(solve(x, n))
