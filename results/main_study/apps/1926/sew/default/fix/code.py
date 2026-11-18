import sys


def  myargsort(a):
    b=list(zip(a, list(range(len(a)))))
    b.sort()
    r = [pr[1] for pr in b]
    return  r

fin = sys.stdin
n = int(fin.readline())
a = [int(number) for number in fin.readline().split()]
p = myargsort(a)
p.reverse()
j = 0
aib = [0] * (n + 1)


def  ultb(x):
    return  -(x^(-x))//2


def  add(p, a, aib, n):
    while n >= p:
        aib[p] += a
        p += ultb(p)
def  suma(p, aib):
    r=0
    while p>0:
        r = r + aib[p]
        p = p - ultb(p)
    return  r

for  i in  range(n):
    add(1 + i, 1, aib, n)
r = [0] * (1 + n)
for  i in  range(n):
    if i > 0 and a[i - 1] > a[i]:
        r[1] += 1
    while  j < n and  a[p[j]] == a[p[i]]:
        add(p[j] + 1, -1, aib, n)
        j = j + 1
    k = 2
    while  k < n and  1 + p[i] * k<n:
        dr, st = min(n, p[i] * k + k + 1), p[i] * k + 2
        r[k] += suma(dr, aib) - suma(st - 1, aib)
        k = k + 1
print(*r[1:n])