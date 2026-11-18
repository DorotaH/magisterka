import sys

u, t = [], set()

p1, m1 = 127, 1000000007

p2, m2 = 131, 1000000009

pow1, pow2 = [1] + [0] * 600005, [1] + [0] * 600005

for i in range(1, 600_005):
    pow1[i] = (pow1[i - 1] * p1) % m1
    pow2[i] = (pow2[i - 1] * p2) % m2


def hash1(n):
    hsh = 0
    for i in range(len(n)):
        hsh = hsh + pow1[i] * ord(n[i])
        hsh = hsh % m1
    return hsh % m1


def hash2(n):
    hsh = 0
    for i in range(len(n)):
        hsh = hsh + pow2[i] * ord(n[i])
        hsh = hsh % m2
    return hsh % m2


a, b = list(map(int, sys.stdin.readline().split()))


def trans(n):
    a = hash1(n)
    b, cyc = hash2(n), ["a", "b", "c"]
    for i in range(len(n)):
        for x in range(3):
            if cyc[x] == n[i]:
                h11 = a - ord(n[i]) * pow1[i] + ord(cyc[(x + 1) % 3]) * pow1[i]
                h12 = b - ord(n[i]) * pow2[i] + ord(cyc[(x + 1) % 3]) * pow2[i]
                h21 = a - ord(n[i]) * pow1[i] + ord(cyc[(x + 2) % 3]) * pow1[i]
                h22 = b - ord(n[i]) * pow2[i] + ord(cyc[(x + 2) % 3]) * pow2[i]
                t.add(((h11 % m1) * m2) + (h12 % m2))
                t.add(((h21 % m1) * m2) + (h22 % m2))


for i in range(a):
    trans(sys.stdin.readline())

for j in range(b):
    inpt = sys.stdin.readline()
    if not hash1(inpt) * m2 + hash2(inpt) in t:
        print("NO")
    else:
        print("YES")
