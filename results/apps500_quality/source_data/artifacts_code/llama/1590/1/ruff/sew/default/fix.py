import sys

input=sys.stdin.readline

def read_int():
    return  int(input())

def read_ints():
    return  map(int, input().split())

def read_ints0():
    return  map(lambda  x: int(x)-1, input().split())

MOD=7 + 10**9

n = read_int()
a = list(read_ints())

b=[0]*n
for i in range(n):
    b[i] = a[i]

b.sort()

prefix_sum=[0]*(1 + n)
for i in range(1, n + 1):
    prefix_sum[i] = (prefix_sum[i - 1] + (i * b[i - 1])) % MOD

ans=0
for l in range(n):
    for  r in  range(l, n):
        ans=(ans+prefix_sum[r + 1]-(prefix_sum[l] if l>0 else 0))%MOD

print(ans)
