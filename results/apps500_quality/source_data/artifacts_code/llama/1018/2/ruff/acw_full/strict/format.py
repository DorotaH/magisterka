n = int(input())
pens = list(map(int, input().split()))

days = 7 * n
for i in range(n):
    days += i + 1

current_day = 1
for i in range(n):
    days_to_use = 6 * (n - i) + (i + 1)
    if days_to_use > pens[i]:
        print(i + 1)
        break
    else:
        current_day += days_to_use
        pens[i] -= days_to_use
