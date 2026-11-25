n = int(input())
s = input()
t = input()

if (s in "ab" and t in "ab") or (s in "bc" and t in "bc") or (s in "ca" and t in "ca"):
    print("NO")
else:
    res = ""
    if s in "ab":
        res += "ac" * (n // 2)
        if n % 2:
            res += "c"
    elif s in "bc":
        res += "ac" * (n // 2)
        if n % 2:
            res += "a"
    else:
        res += "ab" * (n // 2)
        if n % 2:
            res += "c"
    res += (
        (n - res.count("a")) * "a"
        + "b" * (n - res.count("b"))
        + (n - res.count("c")) * "c"
    )
    print("YES")
    print(res)
