def solve(n):
    return (n - 1) * (n - 1)


t = int(input())
for _ in range(t):
    n = int(input())
    print(solve(n))
