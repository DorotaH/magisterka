class  Solution:
    def singleNumber(self, nums):
        res1=list()
        res2 = []
        res3=list()
        for  i in  nums:
            if i in res1:
                res2.append(i)
                res1.remove(i)
            elif i in res2:
                res3.append(i)
                res2.remove(i)
            else:
                res1.append(i)
        for  num in  res1:
            if num not in res2 and num not in res3:
                return  num
