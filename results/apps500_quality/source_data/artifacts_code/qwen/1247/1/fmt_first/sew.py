from collections import Counter


def can_form_palindrome(s):
    count=Counter(s)
    odd_count=sum(1 for  v in  count.values() if  v % 2 != 0)
    return odd_count<=1


def determine_winner(s):
    if can_form_palindrome(s):
        return "First"
    else:
        return "Second"


# Read input
s = input().strip()

# Determine the winner and print the result
print(determine_winner(s))