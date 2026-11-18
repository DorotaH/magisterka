longest_length = {}

class Solution:
    def longestPalindrome(self, s: str) -> int:
        letter_counts = {}
        for char in s:
            letter_counts[char] = 1 + letter_counts.get(char, 0)

        has_odd = False
        num_pairs = 0

        for char, num_letters in letter_counts.items():
            if num_letters % 2 == 1:
                has_odd = True
                num_letters -= 1

            num_pairs += num_letters // 2

        return num_pairs * 2 + has_odd