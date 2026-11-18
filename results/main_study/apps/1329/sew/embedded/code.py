import sys
from  collections import  defaultdict


def  solve():
    input = sys.stdin.readline
    N, primes = int(input()), defaultdict(int)
    ans = 0
    for  i in  range(1, 1 + N):
        k=i
        for j in range(2, 1+i):
            if j ** 2 > i: break
            if 0 == k % j:
                while  0 == k % j:
                    primes[j]+=1
                    k //= j
        if k>1: primes[k]+=1
    P = list()
    for  key in  primes: P.append(primes[key])
    pn = len(P)

    for  i in  range(0, pn):
        if P[i]>=74: ans = ans + 1
        if P[i]>=24:
            for  j in  range(0, pn):
                if P[j] >= 2 and j != i: ans += 1
        if P[i]>=14:
            for  j in  range(0, pn):
                if P[j] >= 4 and j != i: ans += 1
        if P[i]>=4:
            for  j in  range(i+1, pn):
                if P[j] >= 4:
                    for k in range(0, pn):
                        if P[k] >= 2 and i != k and j != k: ans += 1
    print(ans)
    #print(primes)
    #print(P)

    return  0


def  __starting_point():
    solve()
__starting_point()
