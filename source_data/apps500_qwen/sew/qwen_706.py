from collections import Counter


def can_form_palindrome(s):
    # A string can be rearranged into a palindrome if at most one character has an odd count
    return sum(count%2 for count in Counter(s).values())<=1


def determine_winner(s):
    if can_form_palindrome(s):
        return "First"
    else:
        return "Second"

# Read input from standard input
s = input().strip()

# Determine and print the winner
print(determine_winner(s))