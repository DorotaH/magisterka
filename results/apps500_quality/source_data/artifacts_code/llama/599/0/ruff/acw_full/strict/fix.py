s = input()


def is_palindrome(s):
	return s == s[::-1]


def insert_char(s):
	for i in range(len(s)):
		for c in 'abcdefghijklmnopqrstuvwxyz':
			if is_palindrome(s[:i] + c + s[i:]):
				return s[:i] + c + s[i:]
	return 'NA'


print(insert_char(s))
