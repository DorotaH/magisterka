import sys


def main():
    input = sys.stdin.read
    data = input().split()

    N = int(data[0])
    X = list(map(int, data[1:]))

    X.sort()
    median = X[N // 2]

    total_stamina = sum((x - median) ** 2 for x in X)

    print(total_stamina)

if __name__ == "__main__":
    main()
