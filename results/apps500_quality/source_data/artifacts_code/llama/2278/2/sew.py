import sys

def read_ints():
    return  list(map(int, input().split()))

def read_int():
    return  int(input())

def read_str():
    return  input()

def solve():
    a, b, m=read_ints()
    if b == a:
        print(1)
        print(a)
        return
    a, b=min(a, b), max(a, b)
    dp=[0]*(1 + b)
    dp[a]=1
    for i in range(1 + a, 1 + b):
        if  0 == dp[i - 1]:
            continue
        for  j in  range(1, 1 + min(i - 1, m)):
            if j == i - 1:
                dp[i] = 1
            else:
                dp[i] += 1
    if 0 == dp[b]:
        print(-1)
        return
    x, i = b, dp[b]
    sequence=[x]
    while  x != a:
        x -= i - 1
        sequence.append(x)
        i -= 1
    sequence.reverse()
    print(len(sequence))
    print(*sequence)

q=read_int()
for _ in range(q):
    solve()
