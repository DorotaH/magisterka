import sys

n, t = map(int, input().split())
s1 = input()
s2 = input()

if t > n // 2 or t == 0:
    print(-1)
    sys.exit()

ans = ""
diff_count = sum(bool(s1[i] != s2[i]) for i in range(n))
if diff_count == t:
    for c in s1:
        if c == "a":
            ans += "b"
        elif c == "b":
            ans += "a"
        elif c == "c":
            ans += "d"
        else:
            ans += "c"
    print(ans)
elif t == n - diff_count:
    for c in s1:
        ans += "b" if c == "a" else "a"
    print(ans)
else:
    print(-1)
