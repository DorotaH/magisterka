def count_ways(n, m, a, b, s):
	count = 0
	for i in range(n):
		for j in range(m):
			if a[i] == s[0]:
				for k in range(i, n):
					if b[j] == s[m - 1]:
						for l in range(j, m):
							if a[i:k + 1] + b[j:l + 1] == s:
								count += 1
	return count


# Read input
import sys
input = sys.stdin.read
data = input().split()
n = int(data[0])
m = int(data[1])
a = data[2]
b = data[3]
s = data[4]

# Output the result
print(count_ways(n, m, a, b, s))
