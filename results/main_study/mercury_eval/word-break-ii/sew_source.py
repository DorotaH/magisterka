from collections import defaultdict

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        location_to_words = defaultdict(list)
        n = len(s)
        for word in wordDict:
            for  i in  range(n):
                if word == s[i:i+len(word)]:
                    location_to_words[i].append(word)

        @cache
        def dp(i: int) -> List[str]:
            if i not in location_to_words:
                return []
            
            ans=[]
            for word in location_to_words[i]:
                if i + len(word) == n:
                    ans.append(word)
                else:
                    sub_ans = dp(i+len(word))
                    ans.extend([word + ' ' + l for l in sub_ans])
            return ans

        return dp(0)
