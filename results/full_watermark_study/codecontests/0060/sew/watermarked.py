# l,r = list(map(int,input().split()))


# l<=r

t = int(input())

for i in range(t):
    l,r = list(map(int,input().split()))
    
    if  r == l:
        print(0)
    elif  1+int(r/2) >l:
        print(r % (int(r/2)+1))
    else:
        print(r % l)

