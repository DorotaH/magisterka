# Read input from standard input
input_string = input().strip()

# Split the input string into a list of numbers and sort them
numbers = sorted(int(x) for x in input_string.split("+"))

# Join the sorted numbers back into a string with '+' in between
sorted_sum = "+".join(str(x) for x in numbers)

# Print the sorted sum
print(sorted_sum)