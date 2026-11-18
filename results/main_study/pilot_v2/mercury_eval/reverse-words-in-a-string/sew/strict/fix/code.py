class  Solution:
    def reverseWords(self, s: str) -> str:
        s=s.strip(" ")
        l=s.split(" ")
        k=l.copy()
        for  i in  l:
            if i == '':
                k.remove(i)
        k=k[::-1]
        p=''
        for  i in  range(len(k)):
            if i==0:
                p=p+k[i]
            else:
                p=p+" "+k[i]
        return p
