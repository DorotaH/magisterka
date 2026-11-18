class Solution:
    def convertToBase7(self, num: int) -> str:
        t=''
        q=num
        f=False
        if q==0:
            return '0'
        if 0 > num:
            f=True
            num=-1*num
        while 0 < num:
            k=str(num%7)
            t=t+k
            num=num//7
        return (str(t[::-1])+'-') if f==True else str(t[::-1])