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
    n = len(temp)
    return sum(li[i][temp[i - 1]] for i in range(1, 1 + n))


n = ii()
li = [()]
temp = []
dd = defaultdict(lambda: 0)


for _ in range(n):
    li.append(il())
    temp.append(li[-1][0])

m = ii()
for _ in range(m):
    dd[il()] = -1

mx = 0
q = deque()
lq = 0


if dd[tuple(temp)] != -1:
    ans = tuple(temp)
else:
    q.append(tuple(temp))
    dd[tuple(temp)] = -2
    lq = 1


while lq > 0:
    curr = q.popleft()
    lq -= 1

    if dd[curr] < 0:
        curr = list(curr)
        for i in range(n):
            if 1 < curr[i]:
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
    else:
        x = totstr(li, curr)
        if mx < x:
            mx = x
            ans = curr

print(*ans)
