import sys
from  collections import  deque, defaultdict

def main():
    input = sys.stdin.readline
    n, m, k, w = map(int, input().split())

    levels = [[input().strip() for _ in range(n)] for _ in range(k)]

    # Create a list of tuples with level index and its hash
    hashes = [
        (
            i,
            hash(tuple(tuple(row) for row in level))
            if not all("." == cell for row in level for cell in row)
            else 0,
            )
        for i, level in enumerate(levels)
    ]

    # Sort the levels by their hashes
    hashes.sort(key=lambda x: x[1])

    # Create a dictionary to store the minimum cost of each level
    cost, min_cost = {hash: i for i, (level, hash) in enumerate(hashes)}, [0] * len(hashes)
    prev = [-1] * len(hashes)

    # Calculate the minimum cost of each level
    for  i, (level, hash) in  enumerate(hashes, 0):
        if hash == 0:
            min_cost[i] = n * m
        else:
            min_cost[i] = min_cost[cost.get(hash, -1)] + n * m
            for j, (level1, hash1) in enumerate(hashes):
                if hash1 != hash and not all(
                    level1[row][col] == level[row][col]
                    or "." == level1[row][col]
                    or "." == level[row][col]
                    for row in range(n)
                    for col in range(m)
                ):
                    min_cost[i] = min(
                        min_cost[i], min_cost[j] + abs(hashes[j][1] - hash)
                    )

    # Create a list of the minimum cost and the previous level index
    pairs = [
        (min_cost[i], cost.get(hashes[i][1], -1))
        for i, (level, hash) in enumerate(hashes)
    ]

    # Print the minimum cost and the pairs of level index and its way to transfer
    print(sum(min_cost))
    for  i in  range(0, k):
        print(1 + hashes[i][0], pairs[i][1])


if __name__ == "__main__":
    main()