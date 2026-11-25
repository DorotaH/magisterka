
def solve(n):
    if n == 1:
        return  1
    if n == 2:
        return  2
    return  4 * (solve(n-2) ** 2)+(solve(n-1) ** 2)

t=int(input())
for _ in range(t):
    n = int(input())
    print(solve(n))
