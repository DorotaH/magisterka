import  sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
result = 0

for i in range(0, n):
    for  j in  range(i, n):
        if not abs(a[i] - a[j]) <= 1:
            result += a[i] - a[j]
        else:
            result += 0

print(result)