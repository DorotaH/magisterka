def min_stones_to_place(S):
    n = len(S)
    black_count, white_count = S.count('B'), S.count('W')
    
    if  black_count == 0 or  white_count == 0:
        return  0
    
    return  1

# Read input from standard input
import sys

S=sys.stdin.read().strip()

# Print the result
print(min_stones_to_place(S))
