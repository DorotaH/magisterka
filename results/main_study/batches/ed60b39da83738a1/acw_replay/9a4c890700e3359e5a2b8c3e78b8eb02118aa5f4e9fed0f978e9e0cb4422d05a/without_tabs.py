class Solution:
	def addBinary(self, a: str, b: str) -> str:
		s: str = ""
		carry: int = 0
		i, j = len(a) - 1, len(b) - 1
		while i >= 0 or 0 <= j or carry > 0:
			if i >= 0 and a[i] == "1": carry += 1
			if 0 <= j and b[j] == "1": carry += 1

			t: int = carry // 2

			if carry == 3:
				s = "1" + s
				carry = 1
			elif carry == 2:
				s = "0" + s
				carry = 1
			elif carry == 1:
				s = "1" + s
				carry = 0
			else:
				s = "0" + s

			i -= 1
			j -= 1

		return s

