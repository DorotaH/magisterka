import sys

input = sys.stdin.read
data = input().split()

s = data[0]
t = data[1]

def check(i):
    return t * i in s * 2

left = 0
right = 10**6

while left < right:
    mid = (left + right + 1) // 2
    if check(mid):
        left = mid
    else:
        right = mid - 1

if check(left):
    print(left)
else:
    print(-1)
