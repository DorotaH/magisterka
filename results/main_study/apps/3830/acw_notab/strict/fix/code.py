def solve():
    n = int(input())
    s = input()
    k = '-'
    tr = True
    for i in s:
        if k == '-' and i != '-':
            k = i
        if i != '-' and k != i:
            tr = False
    if tr:
        print(n)
        return 0
    ans = sum(bool(s[i] == "-" or s[i - 1] == '-')
          for i in range(n))
    print(ans)


for _ in range(int(input())):
    solve()
