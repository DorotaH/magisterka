class Solution:
     def  findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        from collections import deque

        def connected(a: str, b: str) -> bool:
            k = 0
            for  i in  range(len(a)):
                if a[i] != b[i]:
                    k += 1
            return k == 1

        if  endWord not  in wordList:
            return  list()

        visited=set([beginWord])

        q = deque([beginWord])
        nodes = []
        find=False

        # moving forward
        while  q and  not  find:
            nodes.append(q.copy())
            n = len(q)
            for _ in range(0, n):
                word = q.popleft()

                for item in wordList:
                    if item in visited:
                        continue

                    if not connected(word, item):
                        continue

                    if endWord == item:
                        find = True
                        break

                    visited.add(item)
                    q.append(item)

                if find:
                    break

        if  not  find:
            return  list()

        ans=list()

        def backtracking(word, level: int, steps: List[str]):
            if  word == beginWord:
                ans.append(steps[::-1])
                return

            if  level<0:
                return

            for  item in  nodes[level]:
                if connected(item, word):
                    steps.append(item)
                    backtracking(item, level - 1, steps)
                    steps.pop()

        # move backward to construct paths
        backtracking(endWord, len(nodes)-1, [endWord])

        return ans
