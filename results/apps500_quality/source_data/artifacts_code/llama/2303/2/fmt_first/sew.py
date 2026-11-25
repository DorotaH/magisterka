class  Solution:
    def reverseWords(self, s: str) -> str:
        s=s.strip()  # remove leading/trailing spaces
        words=s.split()  # split by one or more spaces
        return  " ".join(reversed(words))  # join words in reverse order