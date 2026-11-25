import  sys

input = sys.stdin.readline

n = int(input())
h = list(map(int, input().split()))

for i in range(0, n - 1):
    while h[i] + 2<=h[i + 1]:
        h[i]+=1
        h[1 + i]-=1

print(*h)