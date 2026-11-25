from sortedcontainers import SortedSet


def main():
    import sys

    input = sys.stdin.read
    data = input().split()

    N, Q = int(data[0]), int(data[1])
    A, B = (
        [int(data[2 + 2 * i]) for i in range(N)],
        [int(data[3 + 2 * i]) for i in range(N)],
    )
    C, D = (
        [int(data[4 + 2 * i]) for i in range(Q)],
        [int(data[5 + 2 * i]) for i in range(Q)],
    )

    kindergartens = [SortedSet() for _ in range(2 * 10**5 + 1)]

    for i in range(0, N):
        kindergartens[B[i]].add(A[i])

    for j in range(0, Q):
        kindergartens[C[j]].remove(A[C[j] - 1])
        kindergartens[D[j]].add(A[C[j] - 1])
        min_rating = min(k[-1] for k in kindergartens if k)
        print(min_rating)


if __name__ == "__main__":
    main()
