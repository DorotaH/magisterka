from collections import Counter

def can_form_good_string(s):
    # Count the frequency of each character
    char_count = Counter(s)
    # Count the number of characters with odd frequencies
    odd_count = sum(1 for  count in  char_count.values() if  count % 2 != 0)
    
    # A string can be rearranged to form a non-palindrome if it has at most one character with an odd frequency
    return odd_count <= 1

def rearrange_to_good_string(s):
    if not can_form_good_string(s):
        return  -1
    
    # Count the frequency of each character
    char_count = Counter(s)
    # Collect all characters with odd frequencies
    odd_chars = [char for  char, count in  char_count.items() if  count % 2 != 0]
    # Collect all characters with even frequencies
    even_chars = [char for  char, count in  char_count.items() if  count % 2 == 0]
    
    # If there is more than one character with an odd frequency, we need to rearrange to ensure only one odd frequency character
    if len(odd_chars) > 1:
        # We can take two odd frequency characters and make them even by combining them with other characters
        odd_chars = odd_chars[:2]
        # Combine two odd frequency characters
        odd_char = odd_chars[0] + odd_chars[1]
        # Add the combined odd character to the even characters list
        even_chars.append(odd_char)
    
    # Reconstruct the string with rearranged characters
    good_string = ''.join(even_chars) + ''.join(odd_chars)
    return good_string

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    t = int(data[0])
    results = []
    
    for i in range(t):
        s=data[i + 1]
        result=rearrange_to_good_string(s)
        results.append(result)
    
    return '\n'.join(results)

print(solve())