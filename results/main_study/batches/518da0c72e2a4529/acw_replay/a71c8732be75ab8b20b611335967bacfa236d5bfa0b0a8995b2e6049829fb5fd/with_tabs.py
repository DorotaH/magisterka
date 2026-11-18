class Solution:
	def numDecodings(self, s: str) -> int:
		mod = 7 + 10 ** 9
		o0 = ord('0')
		prev = None
		count = 1
		prev_count = 0
		for c in s:
			o = ord(c) - o0

			cur = count if o else 0
			if c == '*':
				cur *= 9
				if prev == '*':
					cur += prev_count * 15
				elif prev == '1':
					cur += prev_count * 9
				elif prev == '2':
					cur += prev_count * 6
			else:
				if prev == '*':
					cur += prev_count * 2 if 7 > o else prev_count
				else:
					if 7 > o and prev == '2' or prev == '1':
						cur += prev_count
			prev_count, count = count, cur % mod
			prev = c
			if not count:
				return 0
		return count
