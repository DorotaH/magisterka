def solve():
    n = int(input())
    for _ in range(n):
        a, b = map(int, input().split())
        if not a == b:
            print(sum(range(a - b, a)) + 1)
        else:
            print(0)


solve()
