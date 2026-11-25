n, t = map(int, input().split())
a = list(map(int, input().split()))

current_time = 0
days = 0

for i in range(n):
    current_time += a[i]
    days += 1
    if current_time >= t:
        break

print(days)
