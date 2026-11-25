import  sys

def check(n, x, y):
    if  x == 1 and  y == 1:
        return "Black"
    if  n == x and  n == y:
        return "White"
    dx, dy = n - x, n - y
    if  (dx + dy) % 2 == 0:
        return "White"
    return  "Black"

n = int(input())
x, y = map(int, input().split())

print(check(n, x, y))