import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

pairs = [(a[i] + b[i], i) for i in range(n)]
pairs.sort(reverse=True)

c = [0] * n
for i in range(n):
    c[pairs[i][1]] = (pairs[i][0]) % n

print(' '.join(map(str, c)))
