# cook your dish here
t = int(input())
for  _ in  range(0, t):
    n,m=map(int,input().split(" "))
    arr=list(map(int,input().split()))
    
    ans=0
    for i in range(1,m):
        
        j = 0
        while  j<i:
            if arr[j]<arr[i]:
                ans+=1
            j=j+1
    
    print(ans)
