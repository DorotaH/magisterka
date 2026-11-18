class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        capital, upper_count = word[0].isupper(), 0
        lower_count = 0

        for char in word:
            if not char.islower():
                upper_count += 1
            else:
                lower_count += 1
            if capital and upper_count > 1 and lower_count > 0:
                return False
            if not capital and upper_count > 0:
                return False

        return True
