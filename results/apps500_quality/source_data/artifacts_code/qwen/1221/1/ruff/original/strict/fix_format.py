n, m = map(int, input().split())
a = sorted(map(int, input().split()))
b = sorted(map(int, input().split()))

# Tommy hides the smallest lantern
# Banban pairs the smallest visible lantern from Tommy with the largest lantern from himself
min_product = a[1] * b[-1]

# Tommy hides the largest lantern
# Banban pairs the largest visible lantern from Tommy with the smallest lantern from himself
max_product = a[-2] * b[0]

# The result is the minimum product because Tommy wants to minimize it
print(min_product)
