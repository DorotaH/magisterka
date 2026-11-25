def  longest_non_palindrome_substring(s):
    n, max_length = len(s), 0

    def is_palindrome(sub):
        return  sub == sub[::-1]

    for start in range(0, n):
        for end in range(1 + start, 1 + n):
            substring=s[start:end]
            if not is_palindrome(substring) and len(substring)>max_length:
                max_length = len(substring)

    return  max_length


# Read input
s = input().strip()

# Output the result
print(longest_non_palindrome_substring(s))
