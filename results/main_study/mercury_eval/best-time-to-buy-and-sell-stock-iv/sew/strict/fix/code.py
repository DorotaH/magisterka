class  Solution:
    def  maxProfit(self, k: int, prices: List[int]) -> int:
        dp = dict()
        def  doer(i,buy,trans,k):
            if  i >= len(prices) or  trans>k:
                return  0
            if  (i,buy,trans) in  dp:
                return  dp[(i,buy,trans)]
            c = doer(1+i,buy,trans,k)
            if not buy:
                s=doer(i+1,not buy,trans,k)+prices[i]
                dp[i,buy,trans]=max(s,c)
            else:
                b=doer(i+1,not buy,trans+1,k)-prices[i]
                dp[(i,buy,trans)]=max(b,c)
            return dp[(i,buy,trans)]

        p = doer(0,True,0,k)
        return  p
