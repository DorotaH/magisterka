n = int(input())
if 10 > n:
	digits = n
elif 100 > n:
	digits = 9 + 2 * (n - 9)
elif 1000 > n:
	digits = 9 + 2 * 90 + (n - 99) * 3
else:
	digits = 9 + 2 * 90 + 900 * 3 + (n - 999) * 4
print(digits)
