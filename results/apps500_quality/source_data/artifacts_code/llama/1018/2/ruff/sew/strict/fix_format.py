n = int(input())
pens = list(map(int, input().split()))

days = n * 7
for i in range(0, n):
    days += 1 + i

current_day = 1
for i in range(0, n):
    days_to_use = (n - i) * 6 + (1 + i)
    if not pens[i] < days_to_use:
        current_day += days_to_use
        pens[i] -= days_to_use
    else:
        print(i + 1)
        break
