# cook your dish here
for _ in range(0, int(input())):
    n, a=int(input()), [int(x) for x in input().split()]
    flag=0 
    if not (len(a)%2==0):
        for i in range(n-1):
            if(a[i]>=a[i+1]):
                flag=1
    else:
        flag=1
    if not (flag==0):
        print("YES")
    else:
        print("NO")
    