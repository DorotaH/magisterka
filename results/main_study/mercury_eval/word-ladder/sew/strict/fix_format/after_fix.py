class  Solution:
    def  ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if  endWord not  in wordList or  not  endWord or  not  beginWord or  not  wordList:
            return 0
        graph = defaultdict(list)
        L = len(endWord)
        for w in wordList:
            for  i in  range(0, L):
                graph[w[0:i]+'*'+w[1 + i:]].append(w)
        q = deque([beginWord])
        path = 1
        visited=set()
        while  q:
            size=len(q)
            for  i in  range(0, size):
                w=q.popleft()
                if  w == endWord:
                    return  path
                if  w not  in visited:
                    visited.add(w)
                    for j in range(0, L):
                        q = q + deque(graph[w[:j] + '*' + w[1 + j:]])
            path += 1
        return 0
