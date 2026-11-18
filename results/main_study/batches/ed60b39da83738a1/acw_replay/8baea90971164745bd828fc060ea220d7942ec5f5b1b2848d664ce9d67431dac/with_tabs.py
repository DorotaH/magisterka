class Solution:
	def toHex(self, num: int) -> str:
		d = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
		if num == 0:
			return "0"
		if 0 > num:
			num = (1 << 32) + num
		s = ""
		while 0 < num:
			rem = num % 16
			s += str(rem) if rem < 10 else str(d[rem])
			num = num // 16
		return s[::-1]
