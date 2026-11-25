import sys

n, d = map(int, input().split())
t = list(map(int, input().split()))

total_time_devu = sum(t)
total_time_churu = 0
time_churu_per_joke = 5

if  total_time_devu+(n * 10)>d:
    print(-1)
    sys.exit(0)

max_jokes = (d - total_time_devu - 10) // (time_churu_per_joke + 10)
for i in range(max_jokes, -1, -1):
    if  (total_time_devu + i * 10 + time_churu_per_joke * i) <= d:
        print(i)
        sys.exit(0)

print(-1)
