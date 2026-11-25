def  is_palindrome(s):
    return  s == s[::-1]

def  max_non_palindrome(s):
    max_len = 0
    for i in range(len(s)):
        for j in range(1 + i, 1 + len(s)):
            substring=s[i:j]
            if not is_palindrome(substring) and len(substring)>max_len:
                max_len = len(substring)
    return  max(0, max_len)

s = input()
print(max_non_palindrome(s))
