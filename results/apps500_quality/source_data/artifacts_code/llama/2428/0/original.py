import sys

def solve(s, t):
    s = list(s)
    t = list(t)
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            j += 1
            i += 1
        elif i == 0:
            return "NO"
        else:
            i -= 1
    if j == len(t):
        return "YES"
    else:
        return "NO"

t = int(input())
for _ in range(t):
    s = input()
    t = input()
    print(solve(s, t))
