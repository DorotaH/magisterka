import sys

n = int(input())
s = n
ans = set()
while s != 0:
    ans.add(s)
    s = 0
    while n - s >= s:
        s += s
    s -= s
print(len(ans))
