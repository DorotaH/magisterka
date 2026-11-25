import sys

input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

odd = [0] * 2
even = [0] * 2
for i in a:
    if i % 2:
        odd[0] += 1
    else:
        even[0] += 1
for i in b:
    if i % 2:
        odd[1] += 1
    else:
        even[1] += 1

ans = 0
if odd[0] >= odd[1]:
    ans += min(odd[0], odd[1])
else:
    ans += odd[0]
if even[0] > odd[1]:
    ans += even[0]
print(ans)
