def insert_to_make_palindrome(s):
    n = len(s)
    for i in range(0, n):
        # Try inserting a character at position i and check if the resulting string is a palindrome
        for char in "abcdefghijklmnopqrstuvwxyz":
            new_s = s[0:i] + char + s[i:]
            if new_s[::-1] == new_s:
                return new_s
    return "NA"


# Read input
s = input().strip()

# Output the result
print(insert_to_make_palindrome(s))
