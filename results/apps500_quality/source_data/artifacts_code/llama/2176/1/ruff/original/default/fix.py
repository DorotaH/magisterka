import sys
from collections import defaultdict

MOD = 998244353
N = int(3e5) + 5

fact = [1] * N
for i in range(1, N):
    fact[i] = (fact[i - 1] * i) % MOD

def bin_power(a, p):
    res = 1
    while p:
        if p & 1:
            res = (res * a) % MOD
        a = (a * a) % MOD
        p >>= 1
    return res

def read_int():
    return int(sys.stdin.readline())

def read_ints():
    return map(int, sys.stdin.readline().split())

def read_string():
    return sys.stdin.readline().strip()

def solve():
    n = read_int()
    pairs = [[read_ints() for _ in range(n)] for _ in range(n)]

    group_a = defaultdict(list)
    group_b = defaultdict(list)

    for i in range(n):
        group_a[pairs[i][0]].append(i)
        group_b[pairs[i][1]].append(i)

    a_groups = set()
    b_groups = set()

    for i in group_a:
        if len(group_a[i]) > 1:
            a_groups.add(tuple(sorted(group_a[i])))
        for j in group_b:
            if len(group_b[j]) > 1:
                b_groups.add(tuple(sorted(group_b[j])))

    a_groups = list(a_groups)
    b_groups = list(b_groups)

    ans = fact[n]
    for i in range(len(a_groups)):
        temp = bin_power(n - len(a_groups[i]), MOD - 2)
        ans *= temp
        ans %= MOD

        for j in b_groups:
            if a_groups[i] & j:
                ans = 0
                break

        for j in a_groups:
            if i != j and (a_groups[i] & j):
                ans = 0
                break

    return ans

print(solve())
