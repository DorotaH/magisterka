from collections import defaultdict
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

odd = [0] * 2
even = [0] * 2
for i in a:
    if not i % 2:
        even[0] += 1
    else:
        odd[0] += 1
for i in b:
    if not i % 2:
        even[1] += 1
    else:
        odd[1] += 1

ans = 0
if odd[0] >= odd[1]:
    ans += min(odd[0], odd[1])
else:
    ans += odd[0]
if odd[1] < even[0]:
    ans += even[0]
print(ans)
