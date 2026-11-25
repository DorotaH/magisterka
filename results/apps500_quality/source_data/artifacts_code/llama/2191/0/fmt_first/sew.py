def solve():
    n = int(input())
    s, ans = input(), [0] * (n + 1)
    cur = 1
    for  i in  range(1, 1 + n):
        cur = 1
        for  j in  range(i, n):
            if s[j]=="0":
                cur += 1
            elif s[j]=="1":
                cur = 1
            else:
                cur=max(cur + 1, 2)
        ans[i] = max(ans[i - 1], cur // (i + 1))
    return  " ".join(map(str, ans[1:]))


print(solve())
