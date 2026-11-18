class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def backtrack(target: int, option: List[int], freq: Dict[int, int]) -> None:

            if 0 == target:
                opt_key = tuple(sorted(freq.items()))
                opts[opt_key] = option
                return

            # Keep exploring
            for num in candidates:
                # if freq[num]>19:
                #     continue
                if target - num < 0:
                    continue
                freq[num] += 1
                backtrack(target - num, option + [num], freq)
                freq[num] -= 1

        opts, freq = dict(), dict()
        for num in candidates:
            freq[num] = 0
        backtrack(target, list(), freq)
        return list(opts.values())
