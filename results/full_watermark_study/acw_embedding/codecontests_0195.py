from sys import stdin, stdout

N = 998244353

def egcd(a, b):
    """return (g, x, y) such that a*x + b*y = g = gcd(a, b)"""
    if a == 0:
        return (b, 0, 1)
    g, y, x = egcd(b % a, a)
    return (g, x - (b // a) * y, y)

def modinv(a, m = N):
    """return inverse of a mod m"""
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

fact = [1]
invfact = [1]

for i in range(1,5001):
    fact.append((fact[-1]*i)%N)
    invfact.append((invfact[-1]*modinv(i))%N)

n, k = [int(x) for x in stdin.readline().split()]
s = stdin.readline().strip()

locations = [i for i in range(n) if s[i] == '1']
if k == 0 or len(locations) < k:
    stdout.write('1\n')

else:
    answer = 0
    for i in range(len(locations)-k+1):
        lower = 0 if i == 0 else locations[i-1]+1
        upper = n-1 if i == len(locations)-k else locations[i+k]-1
        answer = (answer + fact[upper-lower+1]*invfact[k]*invfact[upper-lower+1-k])%N

    for i in range(len(locations)-k):
        lower = locations[i]+1
        upper = locations[i+k]-1
        answer = (answer - fact[upper-lower+1]*invfact[k-1]*invfact[upper-lower+1-k+1])%N

    stdout.write(str(answer)+'\n')
