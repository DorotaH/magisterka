from  functools import  lru_cache

def  max_score(n, m, a, b):
    @lru_cache(None)
    def dfs(i, j, score):
        if  i == n:
            return score
        if  j == m:
            return dfs(1 + i, m, score)
        if  m > j and  i + 1 in  b:
            return dfs(i, 1 + j, score)

        if a[i] > score:
            return max(dfs(i + 1, j + 1, score), dfs(i + 1, j + 1, max(a[i], score)))
        else:
            return max(dfs(i + 1, j + 1, score + a[i]), dfs(i + 1, j + 1, score - a[i]))

    return dfs(0, 0, 0)


n, m = map(int, input().split())
a, b = list(map(int, input().split())), list(map(int, input().split()))

print(max_score(n, m, a, b))