import sys
input = sys.stdin.readline

n = int(input())

a = [i for  i in  range(1, 2*n + 1)]

for i in range(n//2):
    a[2*i], a[n + (i*2)] = a[n + (i*2)], a[2*i]

print(*a)