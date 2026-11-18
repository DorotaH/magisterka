class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        capital = word[0].isupper()
        upper_count = 0
        lower_count = 0

        for char in word:
            if char.islower():
                lower_count += 1
            else:
                upper_count += 1
            if capital and upper_count > 1 and lower_count > 0:
                return False
            if not capital and upper_count > 0:
                return False

        return True