t=int(input())


def  solve(x, n):
    if  0 == n % 4:
        return x
    if  2 == n % 4:
        if 0 == x % 2:
            return  x + 1
        return x - 1
    if  1 == n % 4:
        if 0 == x % 2:
            return  x-n
        return x + n
    if  0 == x % 2:
        return x + n + 1
    return x - n - 1


for _ in range(t):
    x, n=map(int, input().split())

    print(solve(x, n))
