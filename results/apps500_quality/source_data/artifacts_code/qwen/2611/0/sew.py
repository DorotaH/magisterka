def  min_moves(piles):
    piles.sort()
    n, moves = len(piles), 0
    for i in range(n - 1):
        moves += (piles[1 + i] - piles[i]) // 2
    return moves

def  main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    q, piles = int(data[1]), list(map(int, data[2:2+n]))
    queries, index = [], 2 + n
    for _ in range(q):
        t, x = int(data[index]), int(data[index + 1])
        queries.append((t, x))
        index += 2
    
    results = [min_moves(piles)]
    for t, x in queries:
        if t == 0:
            piles.remove(x)
        else:
            piles.append(x)
            piles.sort()
        results.append(min_moves(piles))
    
    for result in results:
        print(result, end=' ')

if __name__ == "__main__":
    main()