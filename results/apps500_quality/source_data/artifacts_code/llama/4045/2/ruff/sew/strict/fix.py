import sys

n = int(sys.stdin.readline())
s, t = sys.stdin.readline().strip(), sys.stdin.readline().strip()

if not ((s[0] != t[0] and s[1] != t[1]) or (s[0] == t[0] and s[1] != t[1]) or (s[0] != t[0] and s[1] == t[1])):
    print("NO")
else:
    print("YES")
    res = ""
    if s[0] == t[0]:
        res = "a" * n + "b" * n + "c" * n
    elif s[0] == t[1]:
        res = "c" * n + "a" * n + "b" * n
    else:
        res = "b" * n + "c" * n + "a" * n
    print(res)
