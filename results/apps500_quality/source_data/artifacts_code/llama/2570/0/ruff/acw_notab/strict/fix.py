def solve():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    return next(
        ("No" for i in range(n) if a[i] + b[i] > x),
        "Yes" if sum(a) <= x else "No",
    )


t = int(input())
for _ in range(t):
    print(solve())
