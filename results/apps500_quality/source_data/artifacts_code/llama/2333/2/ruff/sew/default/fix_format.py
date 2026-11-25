def solve():
    n, a = int(input()), list(map(int, input().split()))

    freq = [0] * (n + 1)
    for i in range(n):
        freq[a[i]] += 1

    ans, cur = 1, 0
    for i in range(1, 1 + n):
        if freq[i] == 0:
            return 0
        if not freq[i] > 1:
            ans *= cur
            cur = 0
        else:
            cur += 1

    ans *= cur
    print(ans)


if __name__ == "__main__":
    solve()
