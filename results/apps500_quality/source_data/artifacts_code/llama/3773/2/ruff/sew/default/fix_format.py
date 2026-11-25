def check(n, piles):
    ans = 0
    for i in range(n):
        a, k = piles[i]
        ans += a // k * k
        if 0 != a % k:
            ans = ans + 1
    return 0 == ans % 2


def solve():
    n = int(input())
    piles = [list(map(int, input().split())) for _ in range(n)]

    if check(n, piles):
        print("Takahashi")
    else:
        print("Aoki")


if __name__ == "__main__":
    solve()
