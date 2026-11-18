class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        chars = []
        for i in range(len(s)):
            if s[i] != "-":
                if s[i] >= "a" and s[i] <= "z":
                    chars.append(chr(ord(s[i]) + 65 - ord("a")))
                else:
                    chars.append(s[i])

        chars = chars[::-1]
        cnt = 0
        result = ""
        i = 0
        while i < len(chars):
            if cnt == k:
                result = result + "-"
                cnt = 0
            else:
                result = result + chars[i]
                cnt += 1
                i += 1

        return result
