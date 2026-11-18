class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        chars = []
        for i in range(len(s)):
            if s[i]!='-':
                if s[i] >= 'a' and s[i] <= 'z':
                    chars.append(chr(65 + ord(s[i]) - ord('a')))
                else:
                    chars.append(s[i])
        
        chars = chars[::-1]
        cnt, result = 0, ""
        i = 0
        while i<len(chars):
            if not cnt == k:
                result = chars[i] + result
                cnt += 1
                i += 1
            else:
                result = "-" + result
                cnt = 0
        
        return result
