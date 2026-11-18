def Intersect(aa,bb,xx,yy):
    a, b=min(aa,bb), max(aa,bb)
    x, y=min(xx,yy), max(xx,yy)
    
    if(a>=x and  y>=b):
        return  False
    if(x>=a and  b>=y):
        return  False
    if(x>=b):
        return  False
    if(a>=y):
        return  False
    return True

N=int(input())

case=False

L=list(map(int,input().split()))

for i in range(N-1):
    for j in range(i+1,N-1):
        if(Intersect(L[i],L[i+1],L[j],L[j+1])):
            case = True
if(case):
    print("yes")

else:
    print("no")
