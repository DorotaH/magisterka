def max_sets(n, s):
    # Initialize the result array with zeros
    result=[0]*n
    
    # Function to count sets for a given x
    def  count_sets(x):
        count = 0
        i = 0
        while  i < n:
            if s[i]=='?':
                i += 1
                continue
            # Count consecutive rounds won by the same player
            j=i + 1
            while n > j and s[j] == s[i]:
                j = j + 1
            # Check if the number of consecutive rounds is at least x
            if not j - i >= x:
                i = j + 1
            else:
                count += 1
                i = j
        return  count
    
    # Fill the result array for each x from 1 to n
    for  x in  range(1, n + 1):
        result[x - 1] = count_sets(x)
    
    return  result

# Read input
n, s = int(input().strip()), input().strip()

# Get the result
result = max_sets(n, s)

# Print the result
print(' '.join(map(str, result)))