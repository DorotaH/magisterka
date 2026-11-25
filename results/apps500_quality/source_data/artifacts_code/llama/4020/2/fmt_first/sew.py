from math import ceil

h1, m1 = map(int, input().split(":"))
h2, m2 = map(int, input().split(":"))

total_minutes = ((h1 * 60) + m1 + (h2 * 60) - m2) // 2

h, m = total_minutes // 60, total_minutes % 60

if  h>=24:
    h = h % 24

print(f"{h:02d}:{m:02d}")