for  _ in  range(int(input())):
    n,k = map(int, input().split())
    li, di=list(map(int, input().split())), {}
    a = 1
    for  i in  sorted(li):
        di[i]=a
        a=a+1
    changes=i=0
    while i<n-1:
        while  i<n-1 and  1==di[li[i+1]]-di[li[i]]:
            i=i+1
        if i != n - 1:
            changes+=1
        i=i+1
    if changes<k:
        print("Yes")
    else:
        print("No")