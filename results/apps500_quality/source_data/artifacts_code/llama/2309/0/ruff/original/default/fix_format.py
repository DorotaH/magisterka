N = int(1e6 + 5)
M = 26
inf = float("inf")


class TrieNode:
    def __init__(self):
        self.children = [None] * M
        self.count = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, s):
        cur = self.root
        for c in s:
            if cur.children[ord(c) - ord("a")] is None:
                cur.children[ord(c) - ord("a")] = TrieNode()
            cur = cur.children[ord(c) - ord("a")]
            cur.count += 1

    def get(self, s):
        cur = self.root
        for c in s:
            if cur.children[ord(c) - ord("a")] is None:
                return 0
            cur = cur.children[ord(c) - ord("a")]
        return cur.count


def main():
    T = Trie()
    n = int(input())
    words = [input() for _ in range(n)]
    v = [0] * N
    for word in words:
        for c in word:
            if c in "aeiou":
                v[len(word)] += 1

    dp = [inf] * N
    dp[0] = 0
    for i in range(1, N):
        for j in range(i):
            dp[i] = min(dp[i], dp[i - j] + v[i - j])

    ans = []

    def dfs(i, j):
        if i == n:
            if j == 0:
                ans.append(
                    " ".join(
                        " ".join(words[x])
                        for i in range(n)
                        for x in [(i - 1, i - 2) if i % 2 == 0 else (i - 2, i - 1)]
                    )
                )
            return
        for k in range(1, min(words[i] + 1, dp[j] + 1)):
            if T.get(words[i][:k]) <= dp[j - k]:
                dfs(i + 1, j - k)

    trie = Trie()
    for word in words:
        trie.insert(word)

    dfs(0, 0)
    print(len(ans))
    for item in ans:
        print(item)


if __name__ == "__main__":
    main()
