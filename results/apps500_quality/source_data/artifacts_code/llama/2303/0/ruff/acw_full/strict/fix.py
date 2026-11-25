class Solution:
	def reverseWords(self, s: str) -> str:
		s = s.strip()  # Remove leading and trailing spaces
		words = s.split()  # Split the string into a list of words
		return ' '.join(reversed(words))  # Join the list of words in reverse order
