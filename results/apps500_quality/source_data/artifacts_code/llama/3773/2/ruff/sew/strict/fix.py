

def  check(n, piles):
    ans=0
    for i in range(n):
        a, k=piles[i]
        ans += a // k * k
        if  a % k != 0:
            ans = ans + 1
    return ans % 2 == 0


def  solve():
    n=int(input())
    piles = [list(map(int, input().split())) for _ in range(n)]

    if check(n, piles):
        print("Takahashi")
    else:
        print("Aoki")

if __name__ == "__main__":
    solve()
