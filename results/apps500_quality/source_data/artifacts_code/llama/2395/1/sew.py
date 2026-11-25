def  find_period(s):
    n = len(s)
    for  k in  range(1, n + 1):
        if  s[:k]*(n//k)==s:
            return  k
    return n


def  solve():
    t = int(input())
    for  _ in  range(t):
        s=input()
        k=find_period(s)
        result=s*(len(s) * 2//k)
        print(result)

solve()