a, b = map(int, input().split())
candles = [a]
hours = a

while len(candles) < b:
	new_candles = sum(candles[i] for i in range(len(candles)))
	candles.extend([new_candles])
	hours += new_candles
	candles.remove(new_candles)

print(hours)
