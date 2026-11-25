def max_alternating_subsequence_length(n, s):
    # Function to calculate the length of the longest alternating subsequence
    def longest_alternating_subsequence(s):
        if not s:
            return 0
        max_len = 1
        current_len = 1
        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                current_len += 1
                max_len = max(max_len, current_len)
            else:
                current_len = 1
        return max_len

    # Calculate the length of the longest alternating subsequence without flipping
    max_len = longest_alternating_subsequence(s)
    
    # Try flipping every possible substring and calculate the longest alternating subsequence
    for i in range(n):
        for j in range(i, n):
            flipped = s[:i] + ''.join('1' if c == '0' else '0' for c in s[i:j+1]) + s[j+1:]
            max_len = max(max_len, longest_alternating_subsequence(flipped))
    
    return max_len

# Read input
n = int(input())
s = input().strip()

# Output the result
print(max_alternating_subsequence_length(n, s))
