n, t = map(int, input().split())
a = list(map(int, input().split()))
total_time = 0
days = 0

for time in a:
    total_time += time
    days += 1
    if  total_time >= t:
        print(days)
        break
    elif  n == days:
        print(n)