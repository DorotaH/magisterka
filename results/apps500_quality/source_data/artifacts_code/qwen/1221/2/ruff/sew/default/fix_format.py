n, m = map(int, input().split())
a, b = list(map(int, input().split())), list(map(int, input().split()))

# Sort the lantern brightnesses
a.sort()
b.sort()

# Tommy will hide the smallest lantern
hidden_lantern = a[0]

# Banban will choose the smallest lantern from Tommy and the largest from himself
min_banban_lantern, max_banban_lantern = b[0], b[-1]

# Calculate the product of the chosen pair
min_product, max_product = (
    hidden_lantern * min_banban_lantern,
    hidden_lantern * max_banban_lantern,
)

# The optimal product is the maximum of the two possible products
optimal_product = max(min_product, max_product)

print(optimal_product)
