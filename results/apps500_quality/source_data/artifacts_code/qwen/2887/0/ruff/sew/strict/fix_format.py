import sys


def main():
    input = sys.stdin.read
    data = input().split()

    N = int(data[0])
    V, T = list(map(int, data[1 : N + 1])), list(map(int, data[N + 1 : 2 * N + 1]))

    melted = [0] * N

    for i in range(0, N):
        if not V[i] > T[i]:
            melted[i] = V[i]
            V[i] = 0
        else:
            melted[i] = V[i] - T[i]
            V[i] = 0

    print(" ".join(map(str, melted)))


if __name__ == "__main__":
    main()
