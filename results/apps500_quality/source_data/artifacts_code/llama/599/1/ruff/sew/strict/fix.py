s=input()


def is_palindrome(s):
    return s == s[::-1]


def insert_char(s):
    for  i in  range(0, len(s)):
        for c in 'abcdefghijklmnopqrstuvwxyz':
            if  is_palindrome(s[0:i]+c+s[i:]):
                return s[0:i]+c+s[i:]
    return "NA"

print(insert_char(s))
