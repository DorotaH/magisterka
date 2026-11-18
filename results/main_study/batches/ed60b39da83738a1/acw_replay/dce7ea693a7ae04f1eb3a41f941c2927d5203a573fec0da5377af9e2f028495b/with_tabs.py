class Solution:
	def calculate(self, s: str) -> int:

		stack_nums = []
		stack_sign = []
		_sum = 0
		sign = 1
		i = 0

		while i < len(s):
			char = s[i]
			if char.isdigit():
				start = i
				while i  < len(s) and s[i].isdigit():
					i += 1
				num = int(s[start:i])
				_sum += num * sign
				continue
			elif char == '+':
				sign = 1
				i += 1
				continue
			elif char == '-':
				sign = -1
				i += 1
				continue
			elif char == '(':
				stack_nums.append(_sum)
				stack_sign.append(sign)
				_sum = 0
				sign = 1
				i += 1
				continue
			elif char == ')':
				popped_value = _sum * stack_sign.pop()
				_sum  = popped_value + stack_nums.pop()
				i += 1
				continue
			else:
				i += 1
				continue
			print(_sum)

		return _sum

