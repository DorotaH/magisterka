def insert_to_make_palindrome(s):
    n = len(s)
    for i in range(n):
        if s[:i][::-1] == s[:i]:
            prefix, suffix = s[:i], s[i:]
            for j in range(26):
                letter = chr(ord("a") + j)
                candidate = prefix + letter + suffix[::-1]
                if candidate == candidate[::-1]:
                    return candidate
    return "NA"


# Read input
s = input().strip()

# Output the result
print(insert_to_make_palindrome(s))
