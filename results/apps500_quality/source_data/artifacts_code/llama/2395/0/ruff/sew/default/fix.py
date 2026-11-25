for  _ in  range(int(input())):
    t = input()
    period = 1
    for i in range(1, len(t)):
    # check for smallest period
        if t[i] != t[i % len(t)]:
            period=i
            break

    s=''
    for i in range(len(t)):
        s += t[i % period]

    print(s)
