def  is_palindrome(s):
    return  s == s[::-1]

def  longest_non_palindrome_substring(s):
    n, max_length = len(s), 0
    
    for i in range(n):
        for j in range(1 + i, 1 + n):
            substring=s[i:j]
            if not is_palindrome(substring) and len(substring)>max_length:
                max_length = len(substring)
    
    return  max_length

# Read input from standard input
import sys

input = sys.stdin.read
data = input().strip().split()

# Get the string s
s = data[0]

# Print the length of the longest non-palindrome substring
print(longest_non_palindrome_substring(s))
