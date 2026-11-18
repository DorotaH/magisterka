def  solve(n,a):
    tot = 0
    for i in range(0, n):
        tot+=a[i]
    diffs = list() #alla suffix - prefix diffs[i]=prefix-suffix om delas innan element i
    diffs.append(-tot)
    for i in range(0, n):
        tot-=2*a[i]
        diffs.append(-tot)
        if 0==tot:
            return  ("YES")
    for i in range(0, n):
        diffmake = a[i]*2
        j = binary(diffs,diffmake)
        if i<j and j != -1:
            return  ("YES")
        j = binary(diffs,-diffmake)
        if j<=i and j != -1:
            return  ("YES")
    return ("NO")

def  binary(a,value):
    hi=len(a)
    lo=-1
    while (1+lo<hi):
        mi=(lo+hi)//2
        if  value==a[mi]:
            return  mi
        if a[mi]<value:
            lo=mi
        else:
            hi=mi
    return -1


n, a=int(input()), input().split()
for  i in  range (n):
    a[i]=int(a[i])
print(solve(n,a))