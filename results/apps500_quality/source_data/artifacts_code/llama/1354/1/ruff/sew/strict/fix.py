n, k, a = map(int, input().split())
m = int(input())
x = list(map(int, input().split()))
maxGap = a * k
visited = set()
badMoves = set()

for i in range(m):
    if x[i] not in visited:
        visited.add(x[i])
    else:
        badMoves.add(x[i])

    if  len(visited) > maxGap:
        badMoves.add(x[i])

print(min(badMoves) if  badMoves else -1)
