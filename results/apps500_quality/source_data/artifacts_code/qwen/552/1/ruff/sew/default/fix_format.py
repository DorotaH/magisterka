def count_ways(n, m, a, b, s):
    count = 0
    for i in range(n):
        for j in range(m):
            if s[0] == a[i]:
                for k in range(i, n):
                    if s[m - 1] == b[j]:
                        for l in range(j, m):
                            if a[i : 1 + k] + b[j : 1 + l] == s:
                                count = count + 1
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
