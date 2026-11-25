n = int(input())
s = input()
t = input()

if not s == t:
    if s in t or t in s:
        print("NO")
    else:
        print("YES")
        a = ['a'] * n
        b = ['b'] * n
        c = ['c'] * n
        res = []
        for _ in range(3):
            res += a
            res += b
            res += c
        print("".join(res))
else:
    print("NO")