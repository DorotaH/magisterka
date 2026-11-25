def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    total_sum = sum(a[i] * 2**i for i in range(n + 1))
    ways = 0

    for i in range(n):
        a_i = a[i]
        if total_sum - 2 * a_i <= 0:
            continue
        if -a_i <= k:
            ways += 1
        if a_i <= k:
            ways += 1

    print(ways)


if __name__ == "__main__":
    solve()
