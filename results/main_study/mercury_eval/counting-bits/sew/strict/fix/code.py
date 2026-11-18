class  Solution:
    def  bits(n):
        k = ''
        while  n > 0:
            p=n%2
            k=k+p
            n//=2
        return  k
    def  countBits(self, n: int) -> List[int]:
        l = [0]
        if  n==0:
            return  l
        for  i in  range(1,n+1):
            k = ''
            while i>0:
                p = i % 2
                k = k + str(p)
                i//=2
            s = k.count('1')
            l.append(s)
        return  l
