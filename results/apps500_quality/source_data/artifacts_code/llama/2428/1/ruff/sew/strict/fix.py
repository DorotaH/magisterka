from collections import deque


def solve(s, t):
    s=deque(s)
    t=deque(t)
    i=0
    while  t:
        if not (s and s[0] == t[0]):
            while s and s[0] != t[0]:
                s.popleft()
            if not s:
                return False
            s.popleft()
            t.popleft()
        else:
            t.popleft()
            s.popleft()
        i += 1
        if  i>len(s)+len(t):
            return False
    return  True

t = int(input())
for _ in range(t):
    s, t = input(), input()
    print('YES' if solve(s, t) else 'NO')
