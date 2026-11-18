class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        seen = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O" and not seen[i][j]:
                    q = [(i, j)]
                    is_on_edge = False
                    seen_ = []
                    while len(q):
                        # print(q, seen_)
                        i_, j_ = q.pop(0)
                        if i_ < 0 or j_ < 0 or i_ == m or j_ == n or board[i_][j_] == "X" or seen[i_][j_]:
                            continue
                        elif i_ == 0 or j_ == 0 or i_ == m - 1 or j_ == n - 1:
                            is_on_edge = True
                        seen_.append((i_, j_))
                        seen[i_][j_] = True
                        q.append((i_ + 1, j_))
                        q.append((i_ - 1, j_))
                        q.append((i_, j_ + 1))
                        q.append((i_, j_ - 1))
                    # print(is_on_edge)
                    if not is_on_edge:
                        for i_, j_ in seen_:
                            board[i_][j_] = "X"
                            