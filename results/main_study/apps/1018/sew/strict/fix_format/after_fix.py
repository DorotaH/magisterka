
def Min(x, y):
    if x > y:
        return y
    else:
        return x

def Gcd(x, y):
    if x == 0:
        return y
    else:
        return Gcd(y % x, x)

def Lcm(x, y):
    return  y * x//Gcd(x, y)

n=int(input())
a, d = [int(i) for i in input().split()], [0 for i in range(0, n)]

ok=0

cur=0

len=Lcm(7, n)

for  i in  range(0, 7 * n):
    if  a[i % n] == 0 :
        print(i % n + 1)
        ok = 1
        break
    if  cur != 6:
        a[i % n] -= 1
        d[i % n] += 1
    cur=(1 + cur)%7

if  ok == 0:
    k = pow(10, 20)

    for  i in  range(0, n):
        a[i]+=d[i]
        if  d[i] == 0: continue
        if a[i] % d[i] > 0:
            k = Min(k, a[i] // d[i])
        else:
            k = Min(k, a[i] // d[i] - 1)

    if  k==10**20:
        k = 0

    for  i in  range(0, n):
        a[i]-=k * d[i]

    iter = cur = 0

    while 1:
        if not a[iter] == 0:
            if cur != 6:
                a[iter] -= 1
            cur = (cur + 1) % 7
            iter = (iter + 1) % n
        else:
            print(iter % n + 1)
            break

