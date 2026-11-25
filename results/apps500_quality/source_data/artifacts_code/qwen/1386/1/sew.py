MOD=998244353

def count_tilings(w, h):
    if  w == 0 or  h == 0:
        return  1
    if  w == 1 and  h == 1:
        return  2
    if  w == 1:
        return  2 * count_tilings(1, h - 1)
    if  h == 1:
        return  2 * count_tilings(w - 1, 1)
    
    a, b = 2, 2
    for  _ in  range(2, h):
        a, b=b, (a+b)%MOD
    for  _ in  range(2, w):
        a, b=b, (a+b)%MOD
    return b*b%MOD

w, h=map(int, input().split())
print(count_tilings(w, h))
