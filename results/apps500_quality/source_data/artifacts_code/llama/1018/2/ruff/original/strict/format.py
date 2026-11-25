n = int(input())
pens = list(map(int, input().split()))

days = n * 7
for i in range(n):
    days += i + 1

current_day = 1
for i in range(n):
    days_to_use = (n - i) * 6 + (i + 1)
    if pens[i] < days_to_use:
        print(i + 1)
        break
    else:
        current_day += days_to_use
        pens[i] -= days_to_use
