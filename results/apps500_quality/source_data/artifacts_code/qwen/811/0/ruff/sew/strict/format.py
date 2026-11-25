a, b = map(int, input().split())
total_hours = a
while b <= a:
    new_candles = a // b
    total_hours += new_candles
    a = a % b + new_candles
print(total_hours)
