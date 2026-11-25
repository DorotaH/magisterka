def is_palindrome(s):
    return s == s[::-1]


def longest_non_palindrome(s):
    n = len(s)
    max_len = 0
    for i in range(n):
        for j in range(i, n):
            substr = s[i:1 + j]
            if not is_palindrome(substr):
                max_len = max(max_len, len(substr))
    return 0 if max_len == 0 else max_len


s = input()
print(longest_non_palindrome(s))
