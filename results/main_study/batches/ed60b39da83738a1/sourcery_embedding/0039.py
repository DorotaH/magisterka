class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        i=0 #g
        j=0 #s
        a=0
        g.sort()
        s.sort()

        while i <= len(g)-1 and j <=len(s)-1:
            if g[i] <= s[j]:
                i +=1
                j +=1
                a +=1
            else:
                j+=1

        print(g)
        print(s)
        return a
        