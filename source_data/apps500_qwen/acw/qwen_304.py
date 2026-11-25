def longest_non_palindrome(s):
	n = len(s)
	max_length = 0
	
	for i in range(n):
		for j in range(i + 1, 1 + n):
			substring = s[i:j]
			if substring != substring[::-1]:
				max_length = max(max_length, len(substring))
				
	return max_length


# Read input from standard input
import sys
input = sys.stdin.read
data = input().split()
s = data[0]

# Output the result
print(longest_non_palindrome(s))
