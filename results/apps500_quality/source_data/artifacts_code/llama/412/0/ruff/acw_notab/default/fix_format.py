n = int(input())
a = list(map(int, input().split()))

max_power = 0
max_count = 0
current_count = 0
for i in range(n):
    current_power = 0
    num = a[i]
    while 1 < num:
        current_power += 1
        num //= 2
    if max_power < current_power:
        max_power = current_power
        max_count = 1
    elif current_power == max_power:
        max_count += 1

print(max_power, max_count)
