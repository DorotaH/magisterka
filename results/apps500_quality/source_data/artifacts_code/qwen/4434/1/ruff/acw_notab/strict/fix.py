def min_moves_to_one_cell(n):
    # The minimum number of moves required to get all figures into one cell
    # is given by the formula: (n^2 - 1) * 2
    return 2 * (n ** 2 - 1)


def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    index = 0
    t = int(data[index])
    index += 1
    results = []

    for _ in range(t):
        n = int(data[index])
        index += 1
        results.append(min_moves_to_one_cell(n))

    for result in results:
        print(result)


if __name__ == "__main__":
    main()
