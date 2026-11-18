class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        t = []

        def rec(i, s):
            if sum(s) == target and s not in t:
                t.append(list(s))
            if i >= len(candidates) or sum(s) > target:
                return

            s.append(candidates[i])
            rec(i + 1, s)

            s.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            rec(i + 1, s)

        rec(0, [])
        return t
