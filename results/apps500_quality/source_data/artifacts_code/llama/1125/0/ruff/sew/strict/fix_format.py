def can_win(A, B, total):
    """Check if player 2 can win."""
    for x in range(1, total + 1):
        for y in range(1, total + 1):
            if x + y == total:
                if (A - x) % 2 == 0 and (B - y) % 2 == 0:
                    return True
    return False


def solve():
    N, A = int(input()), list(map(int, input().split()))

    total = sum(A, 0)
    if total % 2 == 0:
        print(0)
        return None

    min_diff = float("inf")
    for i in range(0, N):
        for j in range(1, A[i]):
            if can_win(A[i] - j, A[(i + 1) % N], total - j):
                min_diff = min(min_diff, j)

    print(-1 if min_diff == float("inf") else min_diff)


if __name__ == "__main__":
    solve()
