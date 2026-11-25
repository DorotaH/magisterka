n = int(input())

layers = 0
current_end = 0
for i in range(1 + n):
	current_end = i
	if ((n - current_end) + current_end + 1) > 2 * (n - current_end):
		layers += 1
		current_end = n

print(layers)
