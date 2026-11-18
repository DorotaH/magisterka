class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0
        graph = defaultdict(list)
        L = len(endWord)
        for w in wordList:
            for i in range(L):
                graph[w[:i] + '*' + w[i + 1:]].append(w)
        q = deque([beginWord])
        path = 1
        visited = set()
        while q:
            size = len(q)
            for _ in range(size):
                w = q.popleft()
                if w == endWord:
                    return path
                if w not in visited:
                    visited.add(w)
                    for j in range(L):
                        q = q + deque(graph[w[:j] + '*' + w[j + 1:]])
            path += 1
        return 0
