
n = int(input())
a = list(map(int, input().split()))

max_xor = 0
current_xor = 0

for i in range(n):
	current_xor = 0
	for j in range(i, n):
		current_xor ^= a[j]
		max_xor = max(max_xor, current_xor)

print(max_xor)
