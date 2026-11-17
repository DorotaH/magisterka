for i in range(0, int(input())):
    n, p, s=int(input()), [int(i) for i in input().split()], input()
    p=sorted(zip(s, p, range(0, n)))
    w=[0]*n
    for  i in  range(0, n):
        w[p[i][2]]=1 + i
    print(*w)
    zip()