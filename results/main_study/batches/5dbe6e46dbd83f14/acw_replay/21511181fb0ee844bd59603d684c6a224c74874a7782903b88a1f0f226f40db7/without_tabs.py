class Solution:
	def countDigitOne(self, n: int) -> int:
		if n == 0:
			return 0
		elif n < 9:
			return 1
		total = (0, 1, 20, 300, 4000, 50000, 600000, 7000000, 80000000, 900000000, )
		chars = str(n)
		result = 0
		if chars[0] == '1':
			result += 1 + int(chars[1:]) + total[len(chars) - 1]
		else:
			result += int(chars[0]) * total[len(chars) - 1] + 10 ** (len(chars) - 1)
		return result if n <= 9 else result + self.countDigitOne(int(chars[1:]))
