from collections import defaultdict
import sys
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
    n = len(s)
    trie = Trie()
    trie.insert(s, "")

    q = int(input())
    queries = []
    for _ in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            queries.append((query[1] - 1, query[2]))
        else:
            queries.append((query[0], query[1] - 1, query[2] - 1))

    visited = set()
    for i in range(n):
        if (i, n) not in visited:
            visited.add((i, n))
            trie.insert(s, i)
        for j in range(i + 1, n):
            if (i, j) not in visited:
                visited.add((i, j))
                trie.insert(s[i:j], i)

    for i, j, k in sorted(queries):
        if i > j:
            print(0)
        else:
            print(trie.query(s[i:j]) - trie.query(s[i - 1:j - 1]))


if __name__ == "__main__":
    main()
