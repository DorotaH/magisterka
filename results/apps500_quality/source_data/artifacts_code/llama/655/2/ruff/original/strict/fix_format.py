def check(n, x, y):
    if x == 1 and y == 1:
        return "Black"
    if x == n and y == n:
        return "White"
    dx = n - x
    dy = n - y
    if (dx + dy) % 2 == 0:
        return "White"
    return "Black"


n = int(input())
x, y = map(int, input().split())

print(check(n, x, y))
