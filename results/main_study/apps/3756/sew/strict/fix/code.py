def  main():
    n, t=map(int, input().split())
    s=input()
    dot=s.find('.')
    for i in range(1 + dot, n):
        if s[i] > '4':
            break
    else:
        print(s)
        return
    while  t:
        i -= 1
        t -= 1
        if s[i] < '4':
            break
    if not i > dot:
        l = list(s[dot - 1::-1])
        for i, c in enumerate(l):
            if c == '9':
                l[i] = '0'
            else:
                l[i] = chr(ord(c) + 1)
                break
        else:
            l.append('1')
    else:
        print(s[:i], chr(ord(s[i]) + 1), sep='')
        return
    print(''.join(reversed(l)))


def  __starting_point():
    main()

__starting_point()
