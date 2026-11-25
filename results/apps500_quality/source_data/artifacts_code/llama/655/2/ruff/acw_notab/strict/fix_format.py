def check(n, x, y):
    if x == 1 and y == 1:
        return "Black"
    if x == n and y == n:
        return "White"
    dx = n - x
    dy = n - y
    return "White" if (dy + dx) % 2 == 0 else "Black"


n = int(input())
x, y = map(int, input().split())

print(check(n, x, y))
