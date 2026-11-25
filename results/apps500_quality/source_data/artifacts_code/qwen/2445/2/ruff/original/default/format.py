def min_turns_to_chess_coloring(n):
    if n % 2 == 0:
        return n // 2
    else:
        return (n // 2) + 1


def main():
    import sys

    input = sys.stdin.read
    data = input().split()

    T = int(data[0])
    results = []

    for i in range(T):
        n = int(data[2 * i + 1])
        results.append(str(min_turns_to_chess_coloring(n)))

    print("\n".join(results))


if __name__ == "__main__":
    main()
