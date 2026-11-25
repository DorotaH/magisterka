n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

min_a = min(a)
max_b = max(b)

min_product = float("inf")
for i in a:
    if i != min_a:
        product = i * min(b)
        min_product = min(min_product, product)

for i in b:
    if i != max_b:
        product = i * min_a
        min_product = min(min_product, product)

print(min_product)
