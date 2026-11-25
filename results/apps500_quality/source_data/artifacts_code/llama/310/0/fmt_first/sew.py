def min_height(n, k):
    k -= n * (n + 1)
    if  k<0:
        return  0
    if k % (n + 1) == 0:
        return k // (n + 1)
    else:
        return k // (n + 1) + 1


n, k=map(int, input().split())
print(min_height(n, k))