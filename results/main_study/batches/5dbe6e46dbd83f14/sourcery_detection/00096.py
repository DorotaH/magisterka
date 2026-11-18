class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        # make a dictionary with lengths and corresponding words in wordDict

        dictt = {}

        for i in wordDict:
            if len(i) in dictt:
                dictt[len(i)].append(i)
            else:
                dictt[len(i)] = [i]

        # print(dictt)

        dp = {}

        def rec(curr):
            if(curr in dp):
                return dp[curr]
            if(curr==len(s)):
                return True
            if(curr>len(s)):
                return False
            flag = False
            for i in dictt:
                if s[curr:curr+i] in dictt[i] and rec(curr+i):
                    flag = True
            dp[curr]=flag
            return flag

        return rec(0)
