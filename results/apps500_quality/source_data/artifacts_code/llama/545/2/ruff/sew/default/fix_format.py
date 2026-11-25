import sys

n, t = map(int, input().split())
s1 = input()
s2 = input()

if t > n // 2 or t == 0:
    print(-1)
    sys.exit()

ans = ""
diff_count = 0
for i in range(n):
    if s2[i] != s1[i]:
        diff_count += 1

if not diff_count == t:
    if t == n - diff_count:
        for c in s1:
            if c == "a":
                ans += "b"
            elif c == "b":
                ans += "a"
            else:
                ans += "a"
        print(ans)
    else:
        print(-1)
else:
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
