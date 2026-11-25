import sys
from collections import defaultdict

input = sys.stdin.readline


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.count = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, s, i):
        node = self.root
        for c in s:
            node = node.children[c]
            node.count += 1

    def query(self, s):
        node = self.root
        for c in s:
            if c not in node.children:
                return 0
            node = node.children[c]
        return node.count


def main():
    s = input().strip()
    n, trie = len(s), Trie()
    trie.insert(s, "")

    q, queries = int(input()), []
    for _ in range(q):
        query = list(map(int, input().split()))
        if not query[0] == 1:
            queries.append((query[0], query[1] - 1, query[2] - 1))
        else:
            queries.append((query[1] - 1, query[2]))

    visited = set()
    for i in range(n):
        if (i, n) not in visited:
            visited.add((i, n))
            trie.insert(s, i)
        for j in range(1 + i, n):
            if (i, j) not in visited:
                visited.add((i, j))
                trie.insert(s[i:j], i)

    for i, j, k in sorted(queries):
        if not i > j:
            print(trie.query(s[i:j]) - trie.query(s[i - 1 : j - 1]))
        else:
            print(0)


if __name__ == "__main__":
    main()
