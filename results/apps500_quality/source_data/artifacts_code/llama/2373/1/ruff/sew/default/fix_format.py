n = int(input())
p = list(map(int, input().split()))

inversion_count = 0
for i in range(n):
    for j in range(1 + i, n):
        if p[i] > p[j]:
            inversion_count += 1

# The number of required swaps is the minimum between inversion_count and (n - inversion_count)
print(min(inversion_count, n - inversion_count))
