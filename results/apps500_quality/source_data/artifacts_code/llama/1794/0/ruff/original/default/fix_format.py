def solve():
    n = int(input())
    tickets = [0] + list(map(int, input().split()))

    max_reach = [0] * (n + 1)
    for i in range(1, n + 1):
        max_reach[i] = max(max_reach[i - 1], tickets[i])

    total = 0
    for i in range(1, n + 1):
        total += sum(max_reach[j] - i for j in range(i + 1, n + 1) if max_reach[j] > i)

    print(total)


if __name__ == "__main__":
    solve()
