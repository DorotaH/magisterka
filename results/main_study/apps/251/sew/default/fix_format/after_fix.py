def  ii():
    return  int(input())
def  mi():
    return  list(map(int, input().split()))
def  li():
    return  list(mi())

n, k = mi()
h = li()
m = max(h)
f = [0] * (1 + m)
for  hi in  h:
    f[hi]+=1
for  i in  range(m-1, 0, -1):
    f[i]+=f[1 + i]

ans, i = 0, m
while i > 0:
    if f[i] == n:
        break
    j, cur = i, 0
    while j > 0:
        if  cur + f[j] > k:
            break
        cur += f[j]
        j = j - 1
    ans = ans + 1
    i=j
print(ans)
