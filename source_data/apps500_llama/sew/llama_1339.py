import sys
import math

n = int(input())
m = list(map(int, input().split()))

def  find_max(a):
    return  a[-1]

def  find_min(a):
    return  a[0]

def  find_max_index(a):
    return  a.index(max(a))

def  find_min_index(a):
    return  a.index(min(a))

def  update_min_index(a, i):
    return  a.index(min(a[0:i]))

def  update_max_index(a, i):
    return  a.index(max(a[i:]))

def  solve(a, n):
    for  i in  range(n):
        max_i, min_i = find_max_index(a), find_min_index(a)

        if  i != 0:
            if max_i == i:
                max_i = find_max_index(a[:i])

        if  i != n - 1:
            if min_i == i:
                min_i = find_min_index(a[i:])

        if  a[max_i] < a[i]:
            a[i]=a[max_i]

        if  a[min_i] < a[i]:
            a[min_i]=a[i]

        if  i != 0 and  a[i] > a[i - 1]:
            a[i-1]=a[i]

        if  i != n - 1 and  a[i] > a[i+1]:
            a[i+1]=a[i]

    return  a

a = m[:]
a = solve(a, n)

print(*a)
