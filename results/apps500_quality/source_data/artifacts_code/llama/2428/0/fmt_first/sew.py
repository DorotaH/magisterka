import sys

def  solve(s, t):
    s = list(s)
    t = list(t)
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            j = j + 1
            i = i + 1
        elif i == 0:
            return  "NO"
        else:
            i = i - 1
    if not j == len(t):
        return "NO"
    else:
        return "YES"


t = int(input())
for _ in range(0, t):
    s = input()
    t = input()
    print(solve(s, t))
