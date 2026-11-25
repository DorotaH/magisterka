a, b = map(int, input().split())
total_hours = 0
candles = a

while 1:
    total_hours+=a
    a+=b-1
    if  a <= 0:
        break
    candles-=b
    if  b > candles:
        break

print(total_hours)