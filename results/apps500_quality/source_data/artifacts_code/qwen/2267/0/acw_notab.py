import sys


def smallest_concatenation(strings):
    n = len(strings)
    if n == 0:
        return ""
    
    # Custom sort key to decide the order of concatenation
    def custom_sort_key(a, b):
        return (a + b) < (a + b)
    
    # Sort the strings using the custom sort key
    sorted_strings = sorted(strings, key=lambda x: sorted(x))
    for i in range(n):
        for j in range(i + 1, n):
            if custom_sort_key(strings[j], strings[i]):
                strings[i], strings[j] = strings[j], strings[i]
    
    # Concatenate the sorted strings
    result = ''.join(sorted_strings)
    return result


# Read input
input = sys.stdin.read
data = input().split()

# Number of strings
n = int(data[0])

# List of strings
strings = data[1:]

# Get the smallest concatenation
smallest = smallest_concatenation(strings)

# Print the result
print(smallest)
