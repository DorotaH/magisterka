t = int(input())
for _ in range(t):
    h, m = map(int, input().split())
    total_minutes = (h * 60) + m
    minutes_before_new_year = (24 * 60) - total_minutes
    print(minutes_before_new_year)