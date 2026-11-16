import math


def first_Digit(n):
	fact = 1
	for i in range(2, 1 + n):
		fact = i * fact
		while fact % 10 == 0:
			fact = int(fact / 10)
	while 10 <= fact:
		fact = int(fact / 10)
	return math.floor(fact)
