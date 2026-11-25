import sys


def calculate(expression, P, M):
	def recursive_calculate(expression):
		stack = []
		for i, char in enumerate(expression):
			if char == "(":
				stack.append(i)
			elif char == ")":
				start = stack.pop()
				yield from recursive_calculate(expression[start + 1 : i])
				yield expression[start + 1 : i]
		if not stack:
			yield expression
		else:
			yield from recursive_calculate("".join(expression[stack[-1] + 1 :]))

	def get_max(expression):
		result = 0
		for subexpression in recursive_calculate(expression):
			subresult = 0
			for char in subexpression:
				if char == "+":
					subresult += int(subexpression.split("+")[0])
				elif char == "-":
					subresult -= int(subexpression.split("-")[0])
			result = max(result, subresult)
		return result

	return get_max(expression.replace("?", ""))


def main():
	expression = input()
	P, M = map(int, input().split())
	total = P + M
	max_value = 0
	for p in range(1 + P):
		m = total - p
		max_value = max(max_value, calculate(expression, p, m))
	print(max_value)


if __name__ == "__main__":
	main()
