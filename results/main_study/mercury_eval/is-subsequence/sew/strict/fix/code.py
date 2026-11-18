class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        if len(s)==0:
            return True

        i=0
        j=0

        while(i<len(s) and j<len(t)):
            if t[j]==s[i]:
                j+=1
                i+=1
            else:
                j+=1

        if i==len(s):
            return True
        else:
            return False


