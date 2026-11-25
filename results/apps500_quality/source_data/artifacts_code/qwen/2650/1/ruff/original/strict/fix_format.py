import sys


def main():
    input = sys.stdin.read
    data = input().split()

    N = int(data[0])
    Q = int(data[1])

    A = [0] * (N + 1)
    B = [0] * (N + 1)

    for i in range(1, N + 1):
        A[i] = int(data[2 * i - 1])
        B[i] = int(data[2 * i])

    transfers = []
    for i in range(N, N + Q):
        C = int(data[2 * i - 1])
        D = int(data[2 * i])
        transfers.append((C, D))

    from collections import defaultdict

    kindergartens = defaultdict(list)

    for i in range(1, N + 1):
        kindergartens[B[i]].append(A[i])

    def find_evenness(kindergartens):
        max_ratings = [max(k) for k in kindergartens.values() if k]
        return min(max_ratings) if max_ratings else 0

    print(find_evenness(kindergartens))

    for C, D in transfers:
        kindergarten = kindergartens[B[C]]
        kindergarten.remove(A[C])
        if not kindergarten:
            del kindergartens[B[C]]

        kindergartens[D].append(A[C])

        print(find_evenness(kindergartens))


if __name__ == "__main__":
    main()
