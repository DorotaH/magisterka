import bisect
import sys


def min_moves_to_cleanup(piles):
    if not piles:
        return 0
    piles.sort()
    n = len(piles)
    left = piles[0]
    right = piles[-1]
    moves = 0
    for i in range(1, n):
        moves += min(piles[i] - left, right - piles[i])
    return moves

def main():
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    q = int(data[1])
    piles = list(map(int, data[2:2+n]))
    queries = [(int(data[2+n+2*i]), int(data[2+n+2*i+1])) for i in range(q)]
    
    results = [min_moves_to_cleanup(piles)]
    
    for t, x in queries:
        if t == 0:
            idx = bisect.bisect_left(piles, x)
            if idx > 0:
                moves = min(piles[idx] - piles[idx-1], piles[-1] - piles[idx])
                results.append(results[-1] - moves)
            if idx < len(piles) - 1:
                moves = min(piles[idx+1] - piles[idx], piles[-1] - piles[idx+1])
                results.append(results[-1] - moves)
            if idx > 0 and idx < len(piles) - 1:
                moves = min(piles[idx] - piles[idx-1], piles[idx+1] - piles[idx])
                results.append(results[-1] - moves)
            piles.remove(x)
        else:
            bisect.insort(piles, x)
            results.append(min_moves_to_cleanup(piles))
    
    for result in results:
        print(result, end=' ')

if __name__ == "__main__":
    main()
