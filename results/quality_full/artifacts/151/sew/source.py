def gcd(p,q):
    while 0 != q:
        p, q=q,p%q
    return p
def is_coprime(x,y):
    return 1 == gcd(x,y)
