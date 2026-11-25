n = int(input())
a = list(map(int, input().split()))

max_power = 0
count = 0

for num in a:
	power = 0
	while num % 2 == 0:
		num //= 2
		power += 1
	if max_power < power:
		max_power = power
		count = 1
	elif power == max_power:
		count += 1

print(max_power, count)
