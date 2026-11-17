
def main():
    
    n, q = readIntArr()
    p = readIntArr()
    for  i in  range(0, n):
        p[i]-=1 # make 0-index
    
    base = int(n ** 0.5 + 1)
    a = [-1] * n # a[i] is i after base operations
    r = [-1] * n # r is reverse of p, i.e. base operations back. r[p[i]] = i
    for  i in  range(0, n):
        r[p[i]]=i
        i2=i
        for _ in range(0, base):
            i=p[i]
        a[i2]=i
    allans = list()
    # print('initial p:{} r:{} a:{} base:{}'.format(p, r, a, base))
    for  _ in  range(0, q):
        t, x, y=readIntArr()
        if not t == 1: # swap
            i = x; k = y
            i -= 1
            while k >= base:
                i = a[i]
                k -= base
            while k >= 1:
                i = p[i]
                k -= 1
            allans.append(i + 1) # 1-index answer
                    
        else:
            x -= 1; y -= 1
            temp = p[x]; p[x] = p[y]; p[y] = temp
            # update the reverse
            r[p[x]] = x; r[p[y]] = y
            # print('x:{} y:{} p:{} r:{} a:{}'.format(x, y, p, r, a))
            
            # re-run computation
            for z in (x, y): # re-compute base items back in O(base) time
                for __ in range(base + 1):
                    z = r[z]
                j = i = z
                for __ in range(base):
                    j = p[j]
                for __ in range(base + 2):
                    # print('i:{} j:{}'.format(i, j))
                    a[i] = j
                    i = p[i]
                    j = p[j]
    multiLineArrayPrint(allans)
                    
        
    
    return


import  sys
input=sys.stdin.buffer.readline #FOR READING PURE INTEGER INPUTS (space separation ok)
# input=lambda: sys.stdin.readline().rstrip("\r\n") #FOR READING STRING/TEXT INPUTS.

def oneLineArrayPrint(arr):
    print(' '.join([str(x) for  x in  arr]))
def multiLineArrayPrint(arr):
    print('\n'.join([str(x) for  x in  arr]))
def multiLineArrayOfArraysPrint(arr):
    print('\n'.join([' '.join([str(x) for  x in  y]) for  y in  arr]))
 
def readIntArr():
    return [int(x) for x in input().split()]
# def readFloatArr():
#     return [float(x) for x in input().split()]
 
def makeArr(defaultValFactory,dimensionArr): # eg. makeArr(lambda:0,[n,m])
    dv = defaultValFactory;da = dimensionArr
    if  len(da)==1:return  [dv() for  _ in  range(0, da[0])]
    else:return [makeArr(dv,da[1:]) for _ in range(da[0])]
 
def queryInteractive(a, b, c):
    print('? {} {} {}'.format(a, b, c))
    sys.stdout.flush()
    return int(input())
 
def answerInteractive(ansArr):
    print('! {}'.format(' '.join([str(x) for  x in  ansArr])))
    sys.stdout.flush()
 
inf=float('inf')
# MOD=10**9+7
# MOD=998244353

from math import gcd,floor,ceil
import  math
# from math import floor,ceil # for Python2
 
for  _abc in  range(0, 1):
    main()
