for _ in range(int(input())):
    s, t = input().strip(), input().strip()
    p = input().strip()

    if not (sorted(s) == sorted(t) and all(
        p.count(char) >= s.count(char) for char in set(s)
    )):
        print("NO")
    else:
        print("YES")