n = int(input())
a = list(map(int, input().split()))

# Function to check if the legend can be true for given x and y


def can_be_true(x, y):
	if y > x:
		x, y = y, x
	return abs(x - y) <= abs(x) and abs(y + x) >= abs(x)


# Count the number of valid pairs
count = 0
for i in range(n):
	for j in range(i + 1, n):
		if can_be_true(a[i], a[j]):
			count += 1

print(count)
