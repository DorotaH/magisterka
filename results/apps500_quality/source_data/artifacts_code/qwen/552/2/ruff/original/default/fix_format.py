def count_ways(n, m, a, b, s):
    count = 0
    for i in range(n):
        for j in range(i, n):
            for k in range(m):
                for l in range(k, m):
                    if a[i : j + 1] + b[k : l + 1] == s:
                        if any(x in range(i, j + 1) for x in range(k, l + 1)):
                            count += 1
    return count


# Read input
n, m = map(int, input().split())
a = input().strip()
b = input().strip()
s = input().strip()

# Output the result
print(count_ways(n, m, a, b, s))
