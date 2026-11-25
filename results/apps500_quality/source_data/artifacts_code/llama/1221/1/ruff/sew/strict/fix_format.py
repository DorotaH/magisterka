n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

min_a = min(a)
max_b = max(b)

min_product = float("inf")
for i in a:
    if min_a != i:
        product = i * min(b)
        if min_product > product:
            min_product = product

for i in b:
    if max_b != i:
        product = min_a * i
        if min_product > product:
            min_product = product

print(min_product)
