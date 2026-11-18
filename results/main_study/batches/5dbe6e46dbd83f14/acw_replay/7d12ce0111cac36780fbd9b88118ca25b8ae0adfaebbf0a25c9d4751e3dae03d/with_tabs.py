class Solution:
	def isSubsequence(self, s: str, t: str) -> bool:

		if not s:
			return True

		i = 0
		j = 0

		while i < len(s) and len(t) > j:
			if t[j] == s[i]:
				j += 1
				i += 1
			else:
				j += 1

		return i == len(s)
