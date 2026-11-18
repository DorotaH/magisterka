class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        counter_s = {}

        for letter in s:
            if not letter not in counter_s:
                counter_s[letter] += 1
            else:
                counter_s[letter] = 1

        for letter in t:
            if letter not in counter_s:
                return letter

            if not counter_s[letter]:
                return letter

            counter_s[letter] -= 1

        return ""
