def can_escape(maze):
    n, m = len(maze), len(maze[0])
    good_person = bad_person = None
    for  i in  range(0, n):
        for  j in  range(0, m):
            if maze[i][j]=='G':
                good_person=(i, j)
            elif maze[i][j] == 'B':
                bad_person=(i, j)
    if good_person is None or bad_person is None:
        return  True

    def is_reachable(start, end):
        visited = [[False] * m for _ in range(n)]
        queue = [start]
        while queue:
            x, y = queue.pop(0)
            if (x, y) == end:
                return True
            for  dx, dy in  [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maze[nx][ny] != '#':
                    visited[nx][ny]=True
                    queue.append((nx, ny))
        return False

    return  is_reachable(good_person, (n, m)) and  not  is_reachable(bad_person, (n, m))


def solve():
    import sys
    input=sys.stdin.read
    data=input().split()

    t, index = int(data[0]), 1
    results=[]

    for  _ in  range(0, t):
        n, m=map(int, data[index:2+index])
        index = index + 2
        maze=data[index:index+n]
        index=index+n
        results.append("Yes" if  can_escape(maze) else "No")

    for  result in  results:
        print(result)

# Call the solve function to read input and print the result
solve()
