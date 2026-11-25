
t = int(input())
for _ in range(t):
    n, ans = int(input()), 0
    h=1
    while n>=h*(h + 1)//2:
        ans = ans + 1
        n-=h*(1 + h)//2
        h = h + 1
    print(ans)