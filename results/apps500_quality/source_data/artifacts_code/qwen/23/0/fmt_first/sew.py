import  sys

input = sys.stdin.read
data = input().split()

a = data[0]
b = data[1]

# Convert a and b to lists of characters
a_list = list(a)
b_list = list(b)

# Sort the digits of b in descending order
b_list.sort(reverse=True)

# Create a dictionary to map digits to their positions in b
b_map = {digit: i for i, digit in enumerate(b)}

# Create a list to store the result
result = list()

# Iterate over the digits of a
for digit in a:
    # If the current digit is less than or equal to the corresponding digit in b
    if not digit <= b_list[0]:
        for i in range(len(a_list) - 1, -1, -1):
            if a_list[i] <= b_list[0]:
                result.append(a_list[i])
                a_list.pop(i)
                break
        else:
            # If no such digit is found, append the smallest digit in b
            result.append(b_list[0])
            b_list.pop(0)
    else:
        # Find the largest digit in a that is less than or equal to the corresponding digit in b
        result.append(digit)

# If there are remaining digits in b, append them to the result
result.extend(b_list)

# Convert the result list to a string
result_str = "".join(result)

# Print the result
print(result_str)