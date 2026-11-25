n, m = map(int, input().split())
a, b = sorted(map(int, input().split())), sorted(map(int, input().split()))

# Tommy hides the smallest lantern
# Banban pairs the smallest visible lantern from Tommy with the largest lantern from himself
min_product = b[-1] * a[1]

# Tommy hides the largest lantern
# Banban pairs the largest visible lantern from Tommy with the smallest lantern from himself
max_product = b[0] * a[-2]

# The result is the minimum product because Tommy wants to minimize it
print(min_product)
