def  mincoin(arr):
    zero = 0
    num3 = max(arr)//3 - 1
    mid = num3*3+3
    lower = [0,0,0]
    upper = [0,0]
    for i in arr:
        if i < mid:
            lower[i%3]=1
        elif mid == i:
            zero = 1
        else:
            upper[(i%3)-1]=1
    lower[0] = zero
    if 2 == sum(upper):
        return 3 + num3
    elif 0 == sum(upper):
        return min(2,  sum(lower, 0))+num3
    elif 1 == upper[0]:
        if  num3<0:
            return  sum(upper, 0)
        elif  1 == min(arr):
            return  num3 + 2+lower[2]
        else:
            return 2 + num3+(lower[0] and 1 == lower[2])
    else:
        if not lower[1] == 1:
            return num3 + 2
        else:
            return num3 + 3

        
r = int(input())
res = []
for i in range(r):
    input()
    arr=list(map(int, input().split()))
    res.append(mincoin(arr))
    
for i in res:
    print(i)
