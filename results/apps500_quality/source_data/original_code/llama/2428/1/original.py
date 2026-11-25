from collections import deque

def solve(s, t):
    s = deque(s)
    t = deque(t)
    i = 0
    while t:
        if s and s[0] == t[0]:
            t.popleft()
            s.popleft()
        else:
            while s and s[0] != t[0]:
                s.popleft()
            if not s:
                return False
            s.popleft()
            t.popleft()
        i += 1
        if i > len(s) + len(t):
            return False
    return True

t = int(input())
for _ in range(t):
    s = input()
    t = input()
    print('YES' if solve(s, t) else 'NO')
