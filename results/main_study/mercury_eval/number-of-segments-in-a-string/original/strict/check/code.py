class Solution:
    def countSegments(self, s: str) -> int:
        s=s.rstrip()
        s=s.lstrip()
        n=len(s)
        p=" "
        s_cnt=0
        for i in range(n):
            if s[i]==' ':
                s_cnt+=1       
        if s_cnt==n:
            return 0
        if s=="":
            return 0
        else:
            c=0
            prev=' '
            for i in range(n-1):
                if s[i]==' ' and prev!=' ':
                    c+=1
                    print(prev, s[i+1], c)
                prev=s[i]
            return c+1
        