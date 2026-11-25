
def  solve():
    n=int(input())
    s = input()
    ans = [0] * (n + 1)
    res=[]
    for  i in  range(1, 1 + n):
        win_count=0
        for  j in  range(i, n):
            if s[j]=='1':
                win_count = win_count + 1
                if i == win_count:
                    res.append(j - i + 1)
                    win_count = 0
        res.append(0)
    for  i in  range(1, 1 + n):
        ans[i]=max(res[:i])
    print(*ans[1:])

solve()