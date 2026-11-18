class  Solution:
    def  getRow(self, rowIndex: int) -> List[int]:
        if rowIndex==0:
            return  [1]
        elif rowIndex==1:
            return  [1,1]
        else:
            b, x=[[1],[1,1]], 1
            while(x<rowIndex):
                a, s=b[x], [1]
                i = 0
                j = i+1
                while(j<len(b[x])):
                    c=0
                    c=c+a[i]+a[j]
                    i+=1
                    j+=1
                    s.append(c)
                s.append(1)
                b.append(s)
                x+=1
        return  b[rowIndex]

