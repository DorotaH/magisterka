from sortedcontainers import SortedList


def min_moves(piles):
    piles = SortedList(piles)
    n = len(piles)
    return 0 if n <= 2 else sum(piles[i] - piles[i - 1] - 1 for i in range(1, n))


def solve():
    import sys
    input = sys.stdin.read
    data = input().split()

    n, q = map(int, data[:2])
    piles = list(map(int, data[2:2 + n]))
    queries = data[2 + n:]

    total_moves = min_moves(piles)
    results = [total_moves]

    i = 0
    while i < 2 * q:
        t = int(queries[i])
        x = int(queries[i + 1])
        i += 2

        if t == 0:
            # Remove a pile
            piles.remove(x)
        else:
            # Add a pile
            piles.add(x)
        total_moves = min_moves(piles)
        results.append(total_moves)

    return results


# Call the solve function and print the results
print(" ".join(map(str, solve())))
