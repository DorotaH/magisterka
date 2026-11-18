"""
Codeforces Contest 266 Div 2 Problem B

Author  : chaotic_iak
Language: Python 3.3.4
"""


def ceildiv(a, b):
	return (1 if a % b else 0) + a // b


def main():
	n, a, b = read()
	s = 6 * n
	if a * b >= s:
		print(a * b)
		print(a, b)
		return
	t = int((6 * n) ** .5)
	tgt = n * 9001
	tgta = 0
	tgtb = 0
	for i in range(1, t + 1):
		c = ceildiv(s, i)
		if i >= a and b <= c and tgt > i * c:
			tgt = i * c
			tgta = i
			tgtb = c
		if i >= b and a <= c and tgt > i * c:
			tgt = i * c
			tgtb = i
			tgta = c
	print(tgt)
	print(tgta, tgtb)

################################### NON-SOLUTION STUFF BELOW


def read(mode=2):
	# 0: String
	# 1: List of strings
	# 2: List of integers
	inputs = input().strip()
	if mode == 0: return inputs
	if mode == 1: return inputs.split()
	if mode == 2: return list(map(int, inputs.split()))


def write(s="\n"):
	if s is None: s = ""
	if isinstance(s, list): s = " ".join(map(str, s))
	s = str(s)
	print(s, end="")


write(main())
