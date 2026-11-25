from collections import Counter


def rearrange_sum(s):
    # Split the input string into individual numbers
    numbers = []
    for num in s.split("+"):
        numbers.append(int(num))
    # Sort the numbers in non-decreasing order
    numbers.sort()
    # Join the sorted numbers back into a string with '+' in between
    return "+".join(map(str, numbers))


# Read input from standard input
input_string = input().strip()
# Print the rearranged sum
print(rearrange_sum(input_string))
