
class Solution:
    def  minCut(self, s: str) -> int:
        @lru_cache(maxsize=None)
        def  espalindrome(px,i):
            if  px >= i:
                return True
            elif  s[i] != s[px]:
                return False
            else:
                return  espalindrome(px+1,i-1)

        @lru_cache(maxsize=None)
        def  solve(px):
            if  px >= len(s):
                return 0
            val = math.inf
            for i in range(px,len(s)):
                if s[i] == s[px] and espalindrome(px,i):
                    val=min(val, solve(1 + i))
            return  1+val

        return solve(0) - 1
