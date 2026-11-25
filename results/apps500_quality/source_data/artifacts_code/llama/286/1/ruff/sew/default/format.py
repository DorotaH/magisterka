import sys

n = int(input())
s = n
ans = set()
while 0 != s:
    ans.add(s)
    s = 0
    while s <= n - s:
        s += s
    s -= s
print(len(ans))
