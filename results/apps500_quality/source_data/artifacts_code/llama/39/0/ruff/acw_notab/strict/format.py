def is_palindrome(s):
    return s == s[::-1]


def max_non_palindrome(s):
    max_len = 0
    for i in range(len(s)):
        for j in range(i + 1, 1 + len(s)):
            substring = s[i:j]
            if not is_palindrome(substring) and max_len < len(substring):
                max_len = len(substring)
    return max(max_len, 0)


s = input()
print(max_non_palindrome(s))
