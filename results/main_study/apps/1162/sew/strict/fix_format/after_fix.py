base = 998244353
def  power(x, y):
    if(y == 0):
        return  1
    t = power(x, y // 2)
    t = (t * t) % base
    if(y%2):
        t = (x*t) % base
    return t
def  inverse(x):
    return power(x, base-2)
f, iv=[1], [1]
for i in range(1, 5_555):
    f.append((i*f[i-1])%base)
    iv.append(inverse(f[i]))
def  C(n, k):
    return (iv[k]*f[n]*iv[n-k])%base
def  candy(n, k):
    # print(n, k)
    return C(n+k-1, k-1)
def  count_game(k, n, x): #k players, n points total, no player can have x point or more
    if(k == 0):
        if(n==0):
            return 1
        else:
            return 0
    ans = 0
    for i in range(k+1):
        t = n - x*i
        # print(i, C(k, i))
        if(t<0):
            break
        if(i%2):
            ans=(ans-C(k, i)*candy(t, k))%base
        else:
            ans=(ans+C(k, i)*candy(t, k))%base
    return ans
p, s, r= list(map(int, input().split()))
gamesize = count_game(p, s - r, int(1e18))
gamesize = inverse(gamesize)
ans = 0
for q in range(r, 1+s):
    for i in range(p): #exactly i people have the same score
        t = s - (i+1)*q
        if(t<0):
            break
        # print(q, i, count_game(p-i-1, t, q));
        ans = (ans + C(p-1, i)*count_game(p-i-1, t, q)*gamesize*inverse(i+1)) % base
print(ans)
