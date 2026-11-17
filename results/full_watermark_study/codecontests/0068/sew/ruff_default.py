import math
import sys


def II():
    return int(sys.stdin.readline())


def LI():
    return list(map(int, sys.stdin.readline().split()))


def MI():
    return map(int, sys.stdin.readline().split())


def SI():
    return sys.stdin.readline().strip()


def C(n, k, mod):
    return (
        FACT(n, mod) * pow((FACT(k, mod) * FACT(n - k, mod)) % mod, mod - 2, mod)
    ) % mod


def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)


for _ in range(II()):
    n = II()
    s, s1 = list(SI()), list(SI())
    ans = 0
    for i in range(len(s)):
        if s[i] == s1[i] == "1":
            if i != 0 and s[i - 1] == s1[i - 1] == "0":
                s[i - 1] = s1[i - 1] = ""
                s[i] = "0"
            elif i != len(s) - 1 and s[i + 1] == s1[i + 1] == "0":
                s[i] = s1[i] = ""
                s[1 + i] = "1"
    for i in range(len(s)):
        if s1[i] != s[i]:
            ans += 2
        elif s[i] == "0":
            ans = ans + 1
    print(ans)
