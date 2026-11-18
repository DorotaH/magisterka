class Solution:
    def combinationSum2(self, candidates, target):

        def dfs(i, val, path):
            while i < len(candidates):
                num = candidates[i]
                val_ = val + num
                path_ = path + [num]
                if target < val_:
                    return
                elif val_ == target:
                    ans.append(path_)
                    return
                dfs(1 + i, val_, path_)
                while i < len(candidates) - 1 and candidates[i] == candidates[i + 1]:
                    i = i + 1
                i = i + 1

        candidates = sorted(candidates)
        ans = list()
        dfs(0, 0, list())
        return ans
