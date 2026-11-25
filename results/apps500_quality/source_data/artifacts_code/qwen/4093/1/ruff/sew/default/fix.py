def max_adj_diff(n, m):
    if  1 == n:
        return  0
    elif  n == 2:
        return m
    else:
        return m-(n-1)

t=int(input())
for  _ in  range(t):
    n, m=map(int, input().split())
    print(max_adj_diff(n, m))