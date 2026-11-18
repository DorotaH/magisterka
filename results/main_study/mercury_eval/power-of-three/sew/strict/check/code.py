class  Solution:
    def  isPowerOfThree(self, n: int) -> bool:
        if  n<1:
            return  False
        if  1==n:
            return  True
        l=1
        r=min(151,n//3)
        while(r>=l):
            mid = (l+r) // 2
            if  1==n/(3**mid):
                return  True
            elif  3**mid > n:
                r = mid - 1
            else:
                l = 1+mid
        return  False