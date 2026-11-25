from sys import stdin, stdout

input = stdin.read
output = stdout.write

data = input().split()

t = int(data[0])
index = 1
results = []

for _ in range(t):
	n = int(data[index])
	k = int(data[1 + index])
	index += 2
	# The k-th positive integer not divisible by n is k + (k // n)
	results.append((k // n) + k)

output('\n'.join(map(str, results)))
