from sys import stdin


def solve():
    n, p, m = map(int, stdin.readline().split())
    days = [0] * (m + 1)
    for _ in range(n):
        d, t = map(int, stdin.readline().split())
        days[d] += t

    balance = 0
    ans = 0
    for i in range(1, m + 1):
        balance += days[i] - p
        if balance < 0:
            ans += 1

    print(ans)


if __name__ == "__main__":
    solve()
