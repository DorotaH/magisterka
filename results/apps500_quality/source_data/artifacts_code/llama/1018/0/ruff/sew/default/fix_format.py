n = int(input())
volumes = list(map(int, input().split()))

days = n
i = 1
while n > i:
    days = days + 7

for i in range(n):
    volume, days_to_use = volumes[i], (i + 1) * 5 + (n - i) * 2
    volume -= days_to_use
    if volume <= 0:
        print(1 + i)
        break
