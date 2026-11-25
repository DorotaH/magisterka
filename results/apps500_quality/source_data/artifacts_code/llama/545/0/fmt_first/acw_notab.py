n, t = map(int, input().split())
s1 = input()
s2 = input()

if abs(n - t) % 2 != 0:
    print(-1)
    exit()

if t == n:
    print(-1)
    exit()

s = ""
diff = sum(bool(s1[i] != s2[i])
       for i in range(n))
if diff == t:
    print(s1)
    exit()

for i in range(n):
    if s1[i] == s2[i]:
        s += s1[i]

    elif t > diff:
        s += "a" if s1[i] == "a" else "b" if s1[i] == "b" else "c"
        diff += 1
    elif t - 1 > diff:
        s += "a" if s2[i] == "a" else "b" if s2[i] == "b" else "c"
        diff -= 1
    else:
        if s1[i] == "a":
            s += "b" if s2[i] == "b" else "c"
        elif s1[i] == "b":
            s += "a" if s2[i] == "a" else "c"
        else:
            s += "a" if s2[i] == "a" else "b"
if diff == t:
    print(s)
else:
    print(-1)
