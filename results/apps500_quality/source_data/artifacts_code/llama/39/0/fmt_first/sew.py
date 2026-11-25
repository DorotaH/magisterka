def  is_palindrome(s):
    return  s == s[::-1]

def  max_non_palindrome(s):
    max_len = 0
    for i in range(0, len(s)):
        for j in range(1 + i, 1 + len(s)):
            substring=s[i:j]
            if not is_palindrome(substring) and len(substring)>max_len:
                max_len = len(substring)
    return  max_len if  max_len>0 else 0


s = input()
print(max_non_palindrome(s))
