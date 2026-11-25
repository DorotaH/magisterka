class Solution:
    def reverseWords(self, s: str) -> str:
        # Split the string into words, removing leading and trailing spaces
        words = [word for word in s.split(" ") if word]
        # Reverse the list of words and join them with a single space
        return " ".join(reversed(words))
