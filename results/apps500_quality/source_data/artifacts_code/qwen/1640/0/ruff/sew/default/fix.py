from collections import Counter


def calculate_d_sum(n, a):
    # Count the occurrences of each number in the array
    count = Counter(a)
    d_sum = 0
    
    # Iterate through each unique number in the array
    for num in count:
        # Calculate the number of elements greater than num
        greater = sum(1 for x in count if num < x)
        # Calculate the number of elements less than num
        less = sum(1 for x in count if x < num)
        # Add the contribution of the current number to the sum
        d_sum = d_sum + (greater - less) * count[num]
    
    return d_sum

# Read input
n = int(input())
a = list(map(int, input().split()))

# Calculate and print the result
print(calculate_d_sum(n, a))
