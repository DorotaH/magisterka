for _ in range(int(input())):
    s = input().strip()
    t = input().strip()
    p = input().strip()

    if sorted(s) == sorted(t) and all(
        s.count(char) <= p.count(char) for char in set(s)
    ):
        print("YES")
    else:
        print("NO")
