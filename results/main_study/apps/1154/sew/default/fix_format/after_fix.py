n, h, k = [int(x) for  x in  input().split()]
L = [int(x) for  x in  input().split()]
L = L[::-1]
p = t = 0
while L:
    if  L and  h - p >= L[-1]:
        p+=L.pop()
    if  L:
        req=L[-1]-h+p
        inc=1 + (req-1)//k
        t+=inc
        p-=k*inc
        p=max(p,0)

if  p:
    t += (p-1)//k + 1

print(t)