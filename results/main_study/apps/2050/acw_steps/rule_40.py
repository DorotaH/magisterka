'''
Created on Oct 12, 2014

@author: Ismael
'''
#import time

from fractions import gcd

def checkSet(setK, newVal):
    return all(gcd(v, newVal) == 1 for v in setK)

def solve(n, k):
    j = 1
    sets = []
    for _ in range(n):
        setK = set()
        while (len(setK) < 4):
            if checkSet(setK, j) and not (not setK and j % 3 == 0):
                setK.add(j)
            j += 1
        sets.append(setK)
    maxV = 0
    for setK in sets:
        maxV = max(maxV, max(setK))
    print(k * maxV)
    for setK in sets:
        print(' '.join([str(k * x) for x in setK]))
    
#t = time.clock()
n, k = list(map(int, input().split()))
solve(n, k)
#print(time.clock()-t)
