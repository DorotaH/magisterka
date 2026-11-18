class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def cond(v):
            res = v//n*n
            if k <= res:
                return True
            for i in range(v//n+1,min(v,m)+1):
                res += v//i
                if k <= res:
                    return True
            return k <= res

        l, r = 1, m * n
        while l < r:
            mid = l + (r-l)//2
            if cond(mid):
                r = mid
            else:
                l = mid + 1
        return l