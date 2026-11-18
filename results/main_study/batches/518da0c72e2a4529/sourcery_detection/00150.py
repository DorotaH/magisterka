class Solution:
	def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
		# Binary search and dynamic programming
		envelopes.sort(key=lambda x: (x[0], -x[1]))
		# Same as 300. Longest Increasing Subsequence
		ans = 0
		dp = [0] * len(envelopes)
		# For each envelope, we get its height and use binary search to find the index where we can insert the current height to maintain the sorted order of the doll set.
		# If the index is beyond the length of the doll set, we add the height to the end of the doll set.
		# Otherwise, we replace the height at that index with the current height, since it can fit inside the previous envelope.
		for _, h in envelopes:
			l = 0
			r = ans
			while l < r:
				m = (l + r) // 2
				if dp[m] >= h:
					r = m
				else:
					l = 1 + m
			dp[l] = h
			if l == ans:
				ans += 1
		return ans 

