n, s = int(input()), input()
t = input()

if not ((s in "ab" and t in "ab") or (s in "bc" and t in "bc") or (s in "ca" and t in "ca")):
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
        "a" * (n - res.count("a"))
        + "b" * (n - res.count("b"))
        + "c" * (n - res.count("c"))
    )
    print("YES")
    print(res)
else:
    print("NO")