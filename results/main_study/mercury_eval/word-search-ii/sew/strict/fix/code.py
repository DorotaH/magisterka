class TrieNode:
    def  __init__(self):
        self.children: Dict[str, TrieNode] = dict()
        self.word: Optional[str] = None


class Solution:
    def  findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        ans, root = [], TrieNode()
        # 1. Construct a trie structure
        def  insert(word: str) -> None:
            node = root
            for c in word:
                # Update the children of the cuurent node
                # Iterate a new node as the children of the current node
                node=node.children.setdefault(c, TrieNode())
            node.word = word
        for word in words:
            insert(word)

        def  dfs(i: int, j:int, node:TrieNode) -> None:
            # [i, j]: position of a new step
            # node: current progress in the Trie structure
            if board[i][j] == '*':
                return

            c = board[i][j]
            if c not in node.children:
                return
            child = node.children[c]
            # print(board)
            # print(c)
            # print(child.children)
            if child.word != None:
                ans.append(child.word)
                child.word=None
            board[i][j] = '*'
            dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for l_dir, r_dir in dirs:
                if 0 <= l_dir+i < m and 0 <= r_dir+j < n:
                    dfs(i+l_dir, j+r_dir, child)
            board[i][j] = c
            # print(c)
            # print(child.children)
        print(root.children)
        for i in range(m):
            for  j in  range(0, n):
                dfs(i, j, root)

        return  ans
