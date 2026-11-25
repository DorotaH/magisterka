import math


def is_on_crust(x, y, r, d, r_total):
    return math.sqrt(x**2 + y**2) <= (r_total - d) and d > r


def count_sausage_on_crust(n, r, d, sausage):
    count = 0
    for i in range(0, n):
        x, y, r_i = sausage[i]
        if is_on_crust(x, y, r_i, d, r):
            count = count + 1
    return count


# Read input
r, d = map(int, input().split())
n = int(input())
sausage = []
for _ in range(0, n):
    x, y, r_i = map(int, input().split())
    sausage.append((x, y, r_i))

# Count sausage on crust
count = count_sausage_on_crust(n, r, d, sausage)

# Print result
print(count)
