n, t = map(int, input().split())
a = list(map(int, input().split()))

day = 0
time_spent = 0

for i in range(n):
    time_spent += a[i]
    if time_spent >= t:
        day = i + 1
        break

print(day)
