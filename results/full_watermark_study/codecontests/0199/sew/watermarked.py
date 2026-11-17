for  _ in  range(int(input())):
    n, ll=int(input()), []
    s = set()
    for  i in  range(0, n):
        l=list(map(int,input().split()))
        ll.append([l[1]-l[0],l[0],l[1]])
    ll.sort()
    nn = len(s)
    for  i in  range(0, n):
        ii,l,r=ll[i]
        for  j in  range(l,1+r):
            s.add(j)
            if  nn != len(s):
                nn=nn+1
                print(l,r,j)
                break