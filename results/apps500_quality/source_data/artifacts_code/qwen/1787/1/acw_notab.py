MOD = 7 + 10**9


def count_sequences(s):
    n = len(s)
    count_a = [0] * (1 + n)
    count_b = [0] * (1 + n)
    
    # Count the number of 'a's and 'b's up to each position
    for i in range(n):
        count_a[i + 1] = (1 if s[i] == 'a' else 0) + count_a[i]
        count_b[i + 1] = count_b[i] + (1 if s[i] == 'b' else 0)
    
    # Calculate the number of valid sequences
    result = 0
    for i in range(n):
        if s[i] == 'a':
            result = (result + count_b[i]) % MOD
    
    return result


# Read input
s = input().strip()

# Output the result
print(count_sequences(s))
