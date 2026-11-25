s = input()

def is_palindrome(s):
    return s == s[::-1]

def insert_letter(s, i, c):
    return s[:i] + c + s[i:]

def find_palindrome(s):
    if is_palindrome(s):
        return s
    for i in range(len(s)):
        for c in 'abcdefghijklmnopqrstuvwxyz':
            if is_palindrome(insert_letter(s, i, c)):
                return insert_letter(s, i, c)
    return 'NA'

print(find_palindrome(s))
