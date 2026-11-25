import sys


def can_win(A, B, total):
    # base cases
    if B > A or A % 2 == B % 2:
        return True
    return (B + 1) * (A - B) <= total


def solve(A):
    # calculate total stones
    total = sum(A)

    # calculate minimum stones to move to guarantee Takahashi's win
    min_move = 0
    for i in range(len(A)):
        if i > 0:
            A[i] += A[0]
        A[0] = 0
        if not can_win(A[i], A[i - 1], total):
            return -1
        min_move = max(min_move, A[0] - 1)

    return min_move


# read input
N = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().strip().split()))

print(solve(A))
