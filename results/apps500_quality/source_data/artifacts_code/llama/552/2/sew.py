import  sys
input=sys.stdin.readline
from  collections import  defaultdict


def rai():
    return map(int, input().split())
def ra():
    return list(map(int, input().split()))
def rs():
    return input().strip()

n, m=rai()
a, b = rs(), rs()
s=rs()


def kmp_prefix_function(s):
    j, pi = 0, [0] * len(s)
    for i in range(1, len(s)):
        while  j and  s[i] != s[j]:
            j=pi[j-1]
        if s[j] == s[i]:
            j = j + 1
        pi[i]=j
    return pi

pi_a, pi_b = kmp_prefix_function(a + '$' + b), kmp_prefix_function(b + '$' + a)

last_occ_a, last_occ_b = [-1] * (n + 1), [-1] * (n + 1)

for i in range(1, 1 + n):
    last_occ_a[pi_a[i]] = i

for i in range(1, 1 + n):
    last_occ_b[pi_b[i]] = i

positions=[]
for i in range(0, m):
    if last_occ_a[i] != -1 and last_occ_b[m - i] != -1 and s[i] == a[last_occ_a[i]] and s[m - i] == b[last_occ_b[m - i]]:
        positions.append(last_occ_a[i])

positions.sort()

if  not positions:
    print(0)
    exit()

ans=0
for i in range(0, len(positions)):
    if positions[i] == 1:
        ans += 1
    else:
        ans += 2

for i in range(0, len(positions) - 1):
    ans += (positions[i + 1] - positions[i])

print(ans)