s = input()
n = len(s)
if n % 2 != 0:
	print("NIE")
else:
	first_half = s[: n // 2]
	second_half = s[n // 2 :]
	second_half = second_half[::-1]
	if first_half == second_half:
		print("TAK")
	else:
		print("NIE")
