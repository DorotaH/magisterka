T = int(input())
for _ in range(T):
    n = int(input())
    B = [int(i) for i in input().split()]
    m = n*(n+1)//2
    if sum(B) % m != 0:
        print("NO")
    else:
        A = sum(B)//m
    
        ans = []
        for i, j in zip(B, B[1:] + [B[0]]):
            ans += [(A + i - j)/n]
    
        if any(int(x) != x or x <= 0 for x in ans):
            print("NO")
        else:
            print("YES")
            print(" ".join(str(int(x)) for x in [ans[-1]] + ans[:-1]))
