class Node:
	def __init__(self):
		self.children = [None] * 26
		self.is_end = False


class Solution:
	def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
		root = Node()
		for word in words:
			cur = root
			for ch in word:
				p = ord(ch) - ord("a")
				if cur.children[p] is None:
					cur.children[p] = Node()
				cur = cur.children[p]
			cur.is_end = True

		ans = []
		for word in words:
			n = len(word)
			dp = [0] * n
			for l in range(n):
				if l == 0 or dp[l - 1] > 0:
					cur = root
					for r in range(l, n):
						p = ord(word[r]) - ord("a")
						if cur.children[p] is None:
							break
						cur = cur.children[p]
						if cur.is_end:
							dp[r] += 1
				if dp[-1] > 1:
					ans.append(word)
					break
		return ans
