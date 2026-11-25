from collections import Counter


def can_form_palindrome(s):
    count = Counter(s)
    odd_count = sum(bool(v % 2 != 0) for v in count.values())
    return odd_count <= 1


def determine_winner(s):
    return "First" if can_form_palindrome(s) else "Second"


# Read input
s = input().strip()

# Determine the winner and print the result
print(determine_winner(s))
