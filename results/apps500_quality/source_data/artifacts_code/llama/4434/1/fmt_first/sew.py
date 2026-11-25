import  math

def min_moves(n):
    return (n * n - 1) * (n * n - 1)


t = int(input())
for _ in range(0, t):
    n = int(input())
    print(min_moves(n))