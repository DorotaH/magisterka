from collections import Counter


def can_form_palindrome(s):
	count = Counter(s)
	odd_count = sum(bool(v % 2 != 0)
				for v in count.values())
	return odd_count <= 1


def determine_winner(s):
	return "First" if can_form_palindrome(s) else "Second"


# Read input from standard input
import sys

s = sys.stdin.read().strip()

# Determine and print the winner
print(determine_winner(s))
