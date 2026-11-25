def solve():
    n = int(input())
    max_val = 2 ** (n - 1)
    for i in range(n - 1):
        max_val = max_val * 10 + 1
    print(str(max_val)[:n])


t = int(input())
for _ in range(t):
    solve()
