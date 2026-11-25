import sys


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def kth_element(x, p, k):
    count = 0
    y = 1 + x
    while True:
        if gcd(p, y) == 1:
            count += 1
            if count == k:
                return y
        y += 1


def main():
    input = sys.stdin.read
    data = input().split()

    t = int(data[0])
    queries = [
        (int(data[i * 3 + 1]), int(data[i * 3 + 2]), int(data[i * 3 + 3]))
        for i in range(t)
    ]

    results = [kth_element(x, p, k) for x, p, k in queries]

    for result in results:
        print(result)


if __name__ == "__main__":
    main()
