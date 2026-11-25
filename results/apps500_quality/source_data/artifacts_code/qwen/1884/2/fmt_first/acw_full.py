import sys

input = sys.stdin.read
data = input().split()

n = int(data[0])
x1 = int(data[1])
x2 = int(data[2])
c = list(map(int, data[3:]))


# Function to check if a given allocation of servers to services is valid
def is_valid_allocation(k1, k2, servers1, servers2):
	total1 = sum(x1 * c[i - 1] / k1 for i in servers1)
	total2 = sum(c[i - 1] * x2 / k2 for i in servers2)
	return x1 <= total1 and x2 <= total2


# Try to find a valid allocation
found = False
for k1 in range(1, 1 + n):
	for k2 in range(1, 1 + n):
		if k1 + k2 > n:
			continue
		servers1 = list(range(1, 1 + k1))
		servers2 = list(range(1 + k1, k1 + k2 + 1))
		if is_valid_allocation(k1, k2, servers1, servers2):
			found = True
			print("Yes")
			print(k1, k2)
			print(*servers1)
			print(*servers2)
			break
	if found:
		break

if not found:
	print("No")
