import sys


def can_insert_to_palindrome(s):
	n = len(s)
	for i in range(n):
		t = s[:i] + s[i + 1 :]
		if t == t[::-1]:
			return True
	return False


def find_insertion(s):
	n = len(s)
	for i in range(n):
		t = s[:i] + s[i + 1 :]
		if t == t[::-1]:
			return s[:i] + s[i] + s[i + 1 :]
	return "NA"


input = sys.stdin.read
data = input().split()

s = data[0]

if can_insert_to_palindrome(s):
	print(find_insertion(s))
else:
	print("NA")
