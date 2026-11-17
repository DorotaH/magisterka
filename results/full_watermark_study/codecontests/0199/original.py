for _ in range(int(input())):
    n=int(input())
    ll=[]
    s=set()
    for i in range(n):
        l=list(map(int,input().split()))
        ll.append([l[1]-l[0],l[0],l[1]])
    ll.sort()
    nn=len(s)
    for i in range(n):
        ii,l,r=ll[i]
        for j in range(l,r+1):
            s.add(j)
            if nn!=len(s):
                nn+=1
                print(l,r,j)
                break