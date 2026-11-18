class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<1:
            return False
        if n==1:
            return True
        l=1
        r=min(151,n//3)
        while(l<=r):
            mid=(l+r)//2
            if n/(3**mid)==1:
                return True
            elif 3**mid>n:
                r=mid-1
            else:
                l=mid+1
        return False
