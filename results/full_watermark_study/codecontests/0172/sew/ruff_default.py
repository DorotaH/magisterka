for _ in range(int(input())):
    n, l = int(input()), list(map(str, input().split()))
    # print(l)
    s = "" + l[0]
    # print(s)
    length = 1
    for i in range(1, len(l)):
        if not (s[length] == l[i][0]):
            s += l[i]
            length += 2
        else:
            s += l[i][1]
            # print(s)
            length += 1
    nm = n - len(s)
    if not (n == 0):
        print(s + "a" * nm)
    else:
        print(s)
