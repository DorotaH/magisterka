import sys

input = sys.stdin.read
data = input().split()

a = data[0]
b = data[1]

# Convert the numbers to lists of digits
a_digits = list(a)
b_digits = list(b)

# Sort the digits of a in descending order
a_digits.sort(reverse=True)

# Try to find the maximum permutation of a that is less than or equal to b
for i in range(len(a_digits)):
    if a_digits[i] < b_digits[i]:
        # Find the largest digit in a that is less than the corresponding digit in b
        for j in range(len(a_digits) - 1, i, -1):
            if b_digits[i] > a_digits[j]:
                # Swap the digits
                a_digits[i], a_digits[j] = a_digits[j], a_digits[i]
                break
        break

# Convert the list of digits back to a string
result = "".join(a_digits)

# Print the result
print(result)
