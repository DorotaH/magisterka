def is_palindrome(s):
    return s == s[::-1]


def longest_non_palindrome(s):
    n = len(s)
    max_len = 0
    for  i in  range(0, n):
        for j in range(i, n):
            substr=s[i:j + 1]
            if  not  is_palindrome(substr):
                max_len=max(max_len, len(substr))
    if  max_len == 0:
        return 0
    return max_len

s=input()
print(longest_non_palindrome(s))
