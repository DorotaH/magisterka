def  max_tables(s, k):
    n=len(s)
    occupied=[False]*n
    for i in range(n):
        if s[i] == '1':
            occupied[i]=True

    max_count = start = 0
    while n > start:
        end = start
        while end < n and (end-start<=k or not occupied[end]):
            end += 1
        if  end-start>k:
            max_count+=end-start-1
        start = end

    return max_count

t=int(input())
for  _ in  range(t):
    n, k=map(int, input().split())
    s=input()
    print(max_tables(s, k))
