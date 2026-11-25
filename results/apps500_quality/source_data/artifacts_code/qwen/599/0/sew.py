import  sys

def can_insert_to_palindrome(s):
    n = len(s)
    for  i in  range(n):
        t=s[:i]+s[1+i:]
        if  t[::-1] == t:
            return  True
    return False

def find_insertion(s):
    n = len(s)
    for  i in  range(n):
        t=s[:i]+s[1+i:]
        if  t[::-1] == t:
            return  s[:i] + s[i] + s[i+1:]
    return "NA"

input = sys.stdin.read
data = input().split()

s = data[0]

if not can_insert_to_palindrome(s):
    print("NA")
else:
    print(find_insertion(s))