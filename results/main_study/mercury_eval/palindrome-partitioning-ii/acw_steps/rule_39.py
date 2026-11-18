
class Solution:
    def minCut(self, s: str) -> int:
        @lru_cache(maxsize=None)
        def espalindrome(px,i):
            if i <= px:
                return True
            elif s[px] != s[i]:
                return False
            else:
                return espalindrome(px+1,i-1)

        @lru_cache(maxsize=None)
        def solve(px):
            if px >= len(s):
                return 0
            val = math.inf
            for i in range(px,len(s)):
                if s[i] == s[px] and espalindrome(px,i):
                    val = min(val, solve(i + 1))
            return val+1

        return solve(0) - 1