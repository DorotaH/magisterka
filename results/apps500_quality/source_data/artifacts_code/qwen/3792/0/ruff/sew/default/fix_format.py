def max_prefixes(n, k, s, t):
    # The maximum number of unique prefixes is the length of the longest common prefix
    # between s and t. This is because any string that is a prefix of s or t and lies
    # within the range [s, t] will be counted in the result.
    max_prefix_length = 0
    for i in range(n):
        if s[i] == t[i]:
            max_prefix_length += 1
        else:
            break

    # The maximum number of unique strings that can be written is the number of
    # unique characters in the range [s, t] plus the length of the longest common prefix.
    # This is because each unique character in the range can be extended with all possible
    # suffixes, and the longest common prefix can be extended with all possible characters.
    max_unique_strings = 1 + max_prefix_length

    return max_unique_strings


# Read input from standard input
n, k = map(int, input().split())
s, t = input().strip(), input().strip()

# Print the result
print(max_prefixes(n, k, s, t))
