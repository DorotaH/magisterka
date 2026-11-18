class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def backtrack(target: int, option: List[int], freq: Dict[int, int]) -> None:

            if target == 0:
                opt_key = tuple(sorted(freq.items()))
                opts[opt_key] = option
                return

            # Keep exploring
            for num in candidates:
                # if freq[num]>19:
                #     continue
                if 0 > target - num:
                    continue
                freq[num] += 1
                backtrack(target - num, [num] + option, freq)
                freq[num] -= 1

        opts = dict()
        freq = dict()
        for num in candidates:
            freq[num] = 0
        backtrack(target, [], freq)
        return list(opts.values())
