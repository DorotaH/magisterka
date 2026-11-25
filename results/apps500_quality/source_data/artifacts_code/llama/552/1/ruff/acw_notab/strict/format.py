import sys

input = sys.stdin.readline


def prefix_function(s):
    n = len(s)
    pi = [0] * (1 + n)
    for i in range(1, n):
        j = pi[i - 1]
        while j and s[i] != s[j]:
            j = pi[j - 1]
        if s[i] == s[j]:
            j += 1
        pi[i] = j
    return pi


def kmp_prefix(s):
    pi = prefix_function(s)
    n = len(s)
    kmp = [0] * (1 + n)
    for i in range(n):
        kmp[i + 1] = pi[i] if s[i] == s[pi[i]] else 0
    return kmp


def solve():
    n, m = map(int, input().split())
    a = input().strip()
    b = input().strip()
    s = input().strip()

    kmp_a = kmp_prefix("$" + a + b)
    kmp_b = kmp_prefix("$" + b + a)
    last = [0] * (1 + n)
    last[1] = 1
    for i in range(2, 1 + n):
        last[i] = last[i - 1]
        if a[i - 1] == s[i - 1]:
            last[i] = 1

    ans = 0
    for i in range(1, n):
        if a[i] == s[i] and kmp_a[i + 1] == m - 1:
            ans += last[i]
        if a[i] == s[m - 1] and kmp_a[i + 1] == m - 1:
            ans += last[i]

    for i in range(n):
        if b[i] == s[i] and kmp_b[i + 1] == m - 1:
            ans += last[i]
        if b[i] == s[m - 1] and kmp_b[i + 1] == m - 1:
            ans += last[i]

    return ans


print(solve())
