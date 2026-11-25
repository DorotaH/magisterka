n = int(input())
a = list(map(int, input().split()))

# Initialize variables
days_in_week = 7
current_day = 0
current_pen = 0

# Loop through the days of the week
for _ in range(days_in_week):
    # Update the current pen and its ink
    current_pen = (1 + current_pen) % n
    if  0 == current_day:
        a[current_pen]-=1
        if 0 == a[current_pen]:
            print(current_pen + 1)
            break
    current_day = (1 + current_day) % days_in_week