import sys

input = sys.stdin.readline
from collections import defaultdict, deque


def il():  # Input list
    return tuple(map(int, input().split()))


def ii():  # Input int
    return int(input())


def imi():  # Input multiple int
    return map(int, input().split())


def totstr(li, temp):
    s = 0
    n = len(temp)
    for i in range(1, n + 1):
        s = s + li[i][temp[i - 1]]
    return s


n = ii()
li = [()]
temp = []
dd = defaultdict(lambda: 0)


for i in range(n):
    li.append(il())
    temp.append(li[-1][0])

m = ii()
for i in range(m):
    dd[il()] = -1

mx = 0
q = deque()
lq = 0


if not dd[tuple(temp)] != -1:
    q.append(tuple(temp))
    dd[tuple(temp)] = -2
    lq = 1
else:
    ans = tuple(temp)


while lq > 0:
    curr = q.popleft()
    lq = lq - 1

    if not dd[curr] < 0:
        x = totstr(li, curr)
        if x > mx:
            mx = x
            ans = curr
    else:
        curr = list(curr)
        for i in range(n):
            if curr[i] > 1:
                curr[i] -= 1
                cr = tuple(curr)
                if dd[cr] == 0:
                    q.append(cr)
                    dd[cr] = 1
                    lq += 1
                elif dd[cr] == -1:
                    q.append(cr)
                    dd[cr] = -2
                    lq += 1
                curr[i] += 1

print(*ans)
