import bisect
n,m=list(map(int,input().split()))
L1=list(map(int,input().split()))
L2=list(map(int,input().split()))
x=int(input())
newL1=[0]
newL2=[0]
for i in L1:newL1.append(i+newL1[-1])
for i in L2:newL2.append(i+newL2[-1])
min1=[]
min2=[]
mx=9999999999999999999
for i in range(1,1+n):
    m1=mx
    for j in range(n-i+1):
        if newL1[i+j]-newL1[j]<m1:m1=newL1[i+j]-newL1[j]
    min1.append(m1)
for i in range(1,1+m):
    m2=mx
    for j in range(m-i+1):
        if newL2[i+j]-newL2[j]<m2:m2=newL2[i+j]-newL2[j]
    min2.append(m2)
area=0
for i in range(n):
    k=x//min1[i]
    for j in range(m):
        if min2[j]>k:break
    if min2[-1]<=k:j+=1
    area = max(area, j*(i+1))
print(area)
