import sys

input=sys.stdin.readline

def  prefix_function(s):
    n=len(s)
    pi=[0]*(1 + n)
    for i in range(1, n):
        j = pi[i - 1]
        while  j and  s[j] != s[i]:
            j=pi[j-1]
        if s[j] == s[i]:
            j = j + 1
        pi[i] = j
    return pi

def  kmp_prefix(s):
    pi, n = prefix_function(s), len(s)
    kmp=[0]*(1 + n)
    for i in range(n):
        kmp[1 + i] = pi[i] if  s[pi[i]] == s[i] else 0
    return kmp

def  solve():
    n, m=map(int, input().split())
    a, b = input().strip(), input().strip()
    s=input().strip()

    kmp_a, kmp_b = kmp_prefix(a + '$' + b), kmp_prefix(b + '$' + a)
    last=[0]*(1 + n)
    last[1]=1
    for i in range(2, 1 + n):
        last[i] = last[i - 1]
        if s[i - 1] == a[i - 1]:
            last[i]=1

    ans=0
    for i in range(1, n):
        if s[i] == a[i]:
            if kmp_a[i + 1]==m-1:
                ans += last[i]
        if s[m - 1] == a[i]:
            if kmp_a[i + 1]==m-1:
                ans += last[i]

    for i in range(n):
        if s[i] == b[i]:
            if kmp_b[i + 1]==m-1:
                ans += last[i]
        if s[m - 1] == b[i]:
            if kmp_b[i + 1]==m-1:
                ans += last[i]

    return ans

print(solve())