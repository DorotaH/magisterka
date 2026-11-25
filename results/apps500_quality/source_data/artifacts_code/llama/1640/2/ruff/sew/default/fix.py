import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

d = 0
for i in range(n):
    for  j in  range(i, n):
        d+=abs(a[i]-a[j])-1 if abs(a[i]-a[j])>1 else 0

print(d)