def longest_alternating_subsequence(s):
    n = len(s)
    # Calculate the length of the longest alternating subsequence without any flips
    max_len = 1
    current_len = 1

    for i in range(1, n):
        if s[i] != s[i - 1]:
            current_len += 1
        else:
            current_len = 1
        max_len = max(max_len, current_len)

    # Try flipping each possible substring and calculate the new longest alternating subsequence
    for i in range(n):
        for j in range(i + 1, n + 1):
            flipped = s[:i] + "".join("0" if c == "1" else "1" for c in s[i:j]) + s[j:]
            new_max_len = 1
            new_current_len = 1
            for k in range(1, len(flipped)):
                if flipped[k] != flipped[k - 1]:
                    new_current_len += 1
                else:
                    new_current_len = 1
                new_max_len = max(new_max_len, new_current_len)
            max_len = max(max_len, new_max_len)

    return max_len


# Read input
n = int(input())
s = input().strip()

# Output the result
print(longest_alternating_subsequence(s))
