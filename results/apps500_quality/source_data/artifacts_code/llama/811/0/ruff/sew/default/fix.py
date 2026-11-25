
a, b = map(int, input().split())

total_time = 0
candles = burnt_candles = 0

while 1:
    if  candles >= a:
        break
    burnt_candles += 1
    candles += 1
    total_time += 1

    if  burnt_candles >= b:
        candles+=burnt_candles
        burnt_candles=0

print(total_time)