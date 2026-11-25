def count_ways(n, m, a, b, s):
    count = 0
    for i in range(n):
        for j in range(i, n):
            for k in range(m):
                for l in range(k, m):
                    if a[i:1 + j] + b[k:l + 1] == s:
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
