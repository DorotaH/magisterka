import sys


def main():
    input = sys.stdin.read
    data = input().split()

    n = int(data[0])
    m = int(data[1])

    k = min(n, m)

    print(k)
    for i in range(k):
        print(i + 1, 1)
    for i in range(k):
        print(1, i + 1)


if __name__ == "__main__":
    main()
