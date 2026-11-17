for _ in range(int(input())):
    s, t = input(), input()
    i, j = len(s) - 1, len(t) - 1
    while i > -1 and -1 < j:
        if s[i] == t[j]:
            i -= 1
            j -= 1
        else:
            i -= 2
    if 0 <= j:
        print("NO")
    else:
        print("YES")
