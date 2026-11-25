def find_pairs(n, a):
    from collections import defaultdict
    
    # Create a dictionary to store the last occurrence of each number
    last = defaultdict(int)
    for i in range(n):
        last[a[i]] = i + 1
    
    # Create a list of indices sorted by the value of a
    indices = sorted(range(n), key=lambda i: a[i])
    
    # Initialize variables to store the result
    max_len = 0
    count = 0
    result = []
    
    # Iterate over the sorted indices
    for i in range(n):
        current = indices[i]
        j = current
        while n > j and a[j] % a[current] == 0:
            j += 1
        length = j - current
        if max_len < length:
            max_len = length
            count = 1
            result = [current + 1]
        elif length == max_len:
            count += 1
            result.append(current + 1)
    
    # Print the result
    print(count, max_len)
    print(*result)


# Read input from standard input
n = int(input())
a = list(map(int, input().split()))

# Call the function with the input
find_pairs(n, a)
