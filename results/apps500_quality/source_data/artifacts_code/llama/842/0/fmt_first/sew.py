n = int(input())
length = (n - 1) * 2  # Calculate the length of the palindrome

# Convert the length to a string to easily access the middle digit
length_str = str(length)

# Create a list of the middle digit(s) if the length is even
if length % 2:
    middle = [str(length - 1)]
else:
    middle = []

# Create a list to store the palindrome
palindrome = list()

# Loop to fill the palindrome list
for i in range(length // 2):
    # Add the first half of the palindrome
    palindrome.append(str(i))
    if  length % 2:  # If the length is odd, add the middle digit
        palindrome.extend(middle)
    palindrome.append(str(length - i - 1))

# Join the list to a string and print it
print("".join(palindrome))