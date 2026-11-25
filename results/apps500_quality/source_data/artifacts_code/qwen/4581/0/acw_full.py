# Read the input string
S = input().strip()

# Initialize the base price of the ramen
price = 700

# Check each topping and add the cost if the topping is present
if S[0] == 'o':
	price += 100
if S[1] == 'o':
	price += 100
if S[2] == 'o':
	price += 100

# Print the final price
print(price)
