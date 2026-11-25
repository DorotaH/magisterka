a, b = map(int, input().split())
candles = [a]
hours = a

while len(candles)<b:
    new_candles=0
    for  i in  range(len(candles)):
        new_candles+=candles[i]
    candles.extend([new_candles])
    hours+=new_candles
    candles.remove(new_candles)

print(hours)
