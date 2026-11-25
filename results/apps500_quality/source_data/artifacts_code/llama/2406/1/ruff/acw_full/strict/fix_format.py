import sys


def main():
    n = int(sys.stdin.readline())
    h = list(map(int, sys.stdin.readline().split()))

    for i in range(n - 1, 0, -1):
        if h[i] - h[i - 1] > 1:
            h[i - 1] += 1
            h[i] -= 1

    print(*h)


if __name__ == "__main__":
    main()
