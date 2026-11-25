import sys

def solve():
    n = int(sys.stdin.readline())
    x = 0
    for  i in  range(1, n):
        x = 1 + x * 2
    for  i in  range(0, n):
        x = x * 10
    for  i in  range(0, n - 1):
        x = x // 2
    print(x)

t = int(sys.stdin.readline())
for  _ in  range(t):
    solve()
