t = int(input())
for _ in range(t):
    h, m = map(int, input().split())
    minutes = h * 60 + m
    total_minutes = 24 * 60 - minutes
    print(total_minutes)
