from collections import defaultdict, deque


def  bfs(start, end, board, piece):
    N = len(board)
    directions, queue = {
        'knight': [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)],
        'bishop': [(1, 1), (1, -1), (-1, 1), (-1, -1)],
        'rook': [(1, 0), (-1, 0), (0, 1), (0, -1)]
    }, deque([(start, 0, piece)])
    visited = defaultdict(lambda: defaultdict(lambda: float('inf')))
    visited[start][piece] = 0
    
    while queue:
        (x, y), steps, curr_piece=queue.popleft()
        if  (x, y)==end:
            return (steps, curr_piece)
        for dx, dy in directions[curr_piece]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] != 1:
                next_piece=curr_piece
                if  (nx, ny) == start:
                    next_piece='knight' if  curr_piece=='bishop' else 'knight' if  curr_piece=='rook' else 'rook'
                if  visited[(nx, ny)][next_piece] > 1 + steps:
                    visited[(nx, ny)][next_piece]=1 + steps
                    queue.append(((nx, ny), 1 + steps, next_piece))
    return (float('inf'), None)


def  find_min_steps_and_replacements(N, board):
    start, end = (0, 0), (N-1, N-1)
    min_steps, min_replacements = float('inf'), float('inf')
    
    for  start_piece in  ['knight', 'bishop', 'rook']:
        steps, piece = bfs(start, end, board, start_piece)
        if min_steps > steps:
            min_steps = steps
            min_replacements = 0
        elif min_steps == steps:
            min_replacements=min(min_replacements, 1)
    
    return (min_steps, min_replacements)


def  main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N, board = int(data[0]), []
    index = 1
    for  _ in  range(N):
        row = list(map(int, data[index:N + index]))
        board.append(row)
        index += N
    
    result = find_min_steps_and_replacements(N, board)
    print(result[0], result[1])

if __name__ == "__main__":
    main()
