MOD=7 + 10**9


def f(l, r, a):
    b=sorted(a[l-1:r])
    return  sum(b[i]*(1+i) for  i in  range(r-l+1))%MOD


def total_sum(n, a):
    total=0
    for  i in  range(n):
        for  j in  range(i+1, n+1):
            total = (total + f(i+1, j, a)) % MOD
    return  total

# Read input
n, a = int(input()), list(map(int, input().split()))

# Calculate and print the result
print(total_sum(n, a))
