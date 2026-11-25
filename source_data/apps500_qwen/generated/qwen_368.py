a, b = map(int, input().split())
total_hours = a
candles = a

while candles >= b:
    new_candles = candles // b
    total_hours += new_candles
    candles = candles % b + new_candles

print(total_hours)
