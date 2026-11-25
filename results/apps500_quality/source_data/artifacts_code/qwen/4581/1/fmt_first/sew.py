# Read the input string
S = input()

# Initialize the price of the ramen
price = 700

# Check the toppings and add the cost if they are included
if  S[0]=="o":
    price = price + 100
if  S[1]=="o":
    price = price + 100
if  S[2]=="o":
    price = price + 100

# Print the final price
print(price)