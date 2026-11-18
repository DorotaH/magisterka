# Enter your code here. Read input from STDIN. Print output to


import math


class ComplexNumber:
	def __init__(self, real, compl):
		self.real = real
		self.compl = compl
		pass

	def __str__(self):
		if (self.compl >= 0):
			return f'{self.real:.2f}' + '+' + f'{self.compl:.2f}' + 'i'
		return f'{self.real:.2f}' + '-' + f'{abs(self.compl):.2f}' + 'i'

	def __add__(x, y):
		return ComplexNumber(y.real + x.real, y.compl + x.compl)

	def __sub__(x, y):
		return ComplexNumber(x.real - y.real, x.compl - y.compl)

	def __mul__(x, y):
		return ComplexNumber(y.real * x.real - y.compl * x.compl, y.real * x.compl + y.compl * x.real)

	def __truediv__(x, y):
		return ComplexNumber((y.real * x.real + y.compl * x.compl) / (y.real * y.real + y.compl * y.compl),
							(y.real * x.compl - y.compl * x.real) / (y.real * y.real + y.compl * y.compl))

	def mod(self):
		return ComplexNumber(math.sqrt(self.real * self.real + self.compl * self.compl), 0)


help = list(map(float, input().split(' ')))
x = ComplexNumber(help[0], help[1])
help = list(map(float, input().split(' ')))
y = ComplexNumber(help[0], help[1])

print(y + x)
print(x - y)
print(y * x)
print(x / y)
print(x.mod())
print(y.mod())
