class  Solution:
    def reverseWords(self, s: str) -> str:
        s=s.strip()  # Remove leading and trailing spaces
        words=s.split()  # Split the string into words
        return  ' '.join(reversed(words))  # Reverse the list of words and join them with a space
