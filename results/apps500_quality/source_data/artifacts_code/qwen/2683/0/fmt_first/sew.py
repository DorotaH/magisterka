def  can_win_in_one_move(N, K, board):
    directions=[(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    def check_winner(player):
        for i in range(0, N):
            for j in range(0, N):
                if  board[i][j]==".":
                    board[i] = board[i][:j] + player + board[i][j + 1 :]
                    for di, dj in directions:
                        count = 1
                        for  k in  range(1, K):
                            ni, nj = i + di * k, j + dj * k
                            if not (0 <= ni < N and 0 <= nj < N and board[ni][nj] == player):
                                break
                            else:
                                count += 1
                        if K == count:
                            board[i]=board[i][:j]+"."+board[i][1 + j :]
                            return  True
                    board[i] = board[i][:j] + "." + board[i][j + 1 :]
        return False

    return "YES" if check_winner("X") else "NO"

def  main():
    import sys

    input=sys.stdin.read
    data=input().split()

    T, index = int(data[0]), 1
    results=list()

    for  _ in  range(T):
        N, K = int(data[index]), int(data[index + 1])
        board = [data[index + 2 + i * N] for i in range(N)]
        index += N * N + 2
        results.append(can_win_in_one_move(N, K, board))

    for  result in  results:
        print(result)


if  __name__ == "__main__":
    main()
