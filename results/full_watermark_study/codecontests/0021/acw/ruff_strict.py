for _ in range(int(input())):
    s, t = input(), input()
    i, j = len(s) - 1, len(t) - 1
    while i > -1 and j > -1:
        if s[i] == t[j]:
            i -= 1
            j -= 1
        else:
            i -= 2
    if j >= 0:
        print("NO")
    else:
        print("YES")
