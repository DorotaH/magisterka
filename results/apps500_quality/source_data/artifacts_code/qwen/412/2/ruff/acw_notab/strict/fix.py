import sys

input = sys.stdin.read
data = input().split()

n = int(data[0])
a = list(map(int, data[1:]))

max_power = 0
count_max_power = 0

for num in a:
    power = 0
    while num % 2 == 0:
        num //= 2
        power += 1
    if max_power < power:
        max_power = power
        count_max_power = 1
    elif power == max_power:
        count_max_power += 1

print(max_power, count_max_power)
