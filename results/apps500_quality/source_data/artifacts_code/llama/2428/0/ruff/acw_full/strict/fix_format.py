def solve(s, t):
    s = list(s)
    t = list(t)
    i, j = 0, 0
    while i < len(s) and len(t) > j:
        if s[i] == t[j]:
            j += 1
            i += 1
        elif i == 0:
            return "NO"
        else:
            i -= 1
    return "YES" if j == len(t) else "NO"


t = int(input())
for _ in range(t):
    s = input()
    t = input()
    print(solve(s, t))
