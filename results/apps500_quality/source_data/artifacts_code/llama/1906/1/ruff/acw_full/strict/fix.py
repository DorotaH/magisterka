n = int(input())
count = 0
for i in range(1, 1 + n):
	is_divisible = any(i % j == 0 for j in range(2, 11))
	if is_divisible:
		count += 1
print(n - count)
