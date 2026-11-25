n = int(input())
total_digits = 0

if 10 > n:
	total_digits = 1 * n
elif 100 > n:
	total_digits = 1 * 9 + 2 * (n - 9)
elif 1000 > n:
	total_digits = 1 * 9 + 2 * 90 + (n - 99) * 3
else:
	total_digits = 1 * 9 + 2 * 90 + 900 * 3 + (n - 999) * 4

print(total_digits)
