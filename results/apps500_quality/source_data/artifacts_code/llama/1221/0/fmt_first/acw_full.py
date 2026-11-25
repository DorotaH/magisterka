import sys

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Find the minimum value in Tommy's lanterns
min_a = min(a)
# Find the maximum value in Banban's lanterns
max_b = max(b)

# Find the minimum value in Tommy's lanterns (excluding the hidden one) and the maximum value in Banban's lanterns
min_product = min(
	b[j] * a[i]
	for i in range(len(a))
	for j in range(len(b))
	if i != a.index(min_a)
)

# Find the maximum product
max_product = max(
	b[j] * a[i]
	for i in range(len(a))
	for j in range(len(b))
	if i != a.index(min_a)
)

print(min(min_product, max_product))
