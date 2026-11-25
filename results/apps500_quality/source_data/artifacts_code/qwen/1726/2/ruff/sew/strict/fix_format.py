n, t = map(int, input().split())
a = list(map(int, input().split()))

day = time_spent = 0

for i in range(n):
    time_spent += a[i]
    if time_spent >= t:
        day = 1 + i
        break

print(day)
