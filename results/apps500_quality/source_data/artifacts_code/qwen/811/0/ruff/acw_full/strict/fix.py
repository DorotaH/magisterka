a, b = map(int, input().split())
total_hours = a
while a >= b:
	new_candles = a // b
	total_hours += new_candles
	a = new_candles + a % b
print(total_hours)
