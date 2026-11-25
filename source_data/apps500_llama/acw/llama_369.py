a, b = map(int, input().split())
total_hours = 0
candles = a

while True:
	total_hours += a
	a += b - 1
	if a <= 0:
		break
	candles -= b
	if candles < b:
		break

print(total_hours)
