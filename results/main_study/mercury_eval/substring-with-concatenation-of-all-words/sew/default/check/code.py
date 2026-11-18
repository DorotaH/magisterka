class Solution:
    def  findSubstring(self, s: str, words: List[str]) -> List[int]:
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or words==list(): return

        lenstr = len(s)
        lenword = len(words[0])
        lensubstr=lenword*len(words)

        times=dict()
        # frequency 
        for  word in  words:
            if word in times:
                times[word] += 1 
            else:
                times[word] = 1
        ans=list()
        for  i in  range(min(lenword, lenstr - lensubstr+1)):
            self.findAnswer(i, lenstr, lenword, lensubstr, s, times, ans)
        return ans
         


    def  findAnswer(self,strstart,lenstr,lenword,lensubstr,s,times,ans):
        wordstart=strstart
        curr={}
        while strstart+lensubstr<=lenstr:
            word=s[wordstart:wordstart+lenword]
            wordstart+=lenword
            if not word not in times:
                if word in curr:
                    curr[word]+=1
                else:
                    curr[word]=1
                while curr[word]>times[word]:
                    curr[s[strstart:strstart+lenword]]-=1
                    strstart+=lenword
                if wordstart-strstart==lensubstr:
                    ans.append(strstart)
            else:
                strstart=wordstart
                curr.clear()