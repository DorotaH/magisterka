n = int(input())
if n < 10:
	digits = n
elif n < 100:
	digits = 9 + 2 * (n - 9)
elif n < 1000:
	digits = 9 + 2 * 90 + (n - 99) * 3
else:
	digits = 9 + 2 * 90 + 900 * 3 + (n - 999) * 4
print(digits)
