T = int(input())
for _ in range(0, T):
    n, B = int(input()), [int(i) for i in input().split()]
    m = n * (1 + n) // 2
    if not sum(B) % m != 0:
        A = sum(B) // m

        ans = []
        for i, j in zip(B, B[1:] + [B[0]]):
            ans += [(A + i - j) / n]

        if any(int(x) != x or x <= 0 for x in ans):
            print("NO")
        else:
            print("YES")
            print(" ".join(str(int(x)) for x in [ans[-1]] + ans[:-1]))
    else:
        print("NO")
