class Solution:
    def numDecodings(self, s: str) -> int:
        @lru_cache(maxsize=None)
        def helper(index):
            if index == len(s):
                return 1
            if s[index] == '0':
                return 0
            if index == len(s) - 1:
                return 1
            res = helper(1 + index)

            if int(s[index: 2 + index]) <= 26:
                res += helper(2 + index)
            return res
        res = helper(0)
        return res
