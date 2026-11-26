from sortedcontainers import SortedList


def min_moves(piles):
    piles = SortedList(piles)
    n = len(piles)
    if n <= 2:
        return 0
    total_moves = 0
    for i in range(1, n):
        total_moves += piles[i] - piles[i - 1] - 1
    return total_moves


def solve():
    import sys

    input = sys.stdin.read
    data = input().split()

    n, q = map(int, data[0:2])
    piles, queries = list(map(int, data[2 : 2 + n])), data[2 + n :]

    total_moves = min_moves(piles)
    results = [total_moves]

    i = 0
    while i < 2 * q:
        t, x = int(queries[i]), int(queries[i + 1])
        i = i + 2

        if t == 0:
            # Remove a pile
            piles.remove(x)
            total_moves = min_moves(piles)
        else:
            # Add a pile
            piles.add(x)
            total_moves = min_moves(piles)

        results.append(total_moves)

    return results


# Call the solve function and print the results
print(" ".join(map(str, solve())))
