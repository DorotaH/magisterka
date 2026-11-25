def max_pyramids(n):
    total_pyramids = 0
    while n >= 1:
        h = 1
        while (h * (h + 1)) // 2 <= n:
            h += 1
        h -= 1
        total_pyramids += 1
        n -= (h * (h + 1)) // 2
    return total_pyramids


def main():
    import sys

    input = sys.stdin.read
    data = input().split()

    t = int(data[0])
    results = []
    index = 1
    for _ in range(t):
        n = int(data[index])
        index += 1
        results.append(max_pyramids(n))

    for result in results:
        print(result)


if __name__ == "__main__":
    main()
