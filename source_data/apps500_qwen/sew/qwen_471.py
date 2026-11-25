def determine_winner(s):
    n=len(s)
    if n<=2:
        return  "First"
    
    # Check if the string can be reduced to a single character by removing all characters
    for i in range(1, n-1):
        if s[i] != s[i-1] and s[i] != s[i+1]:
            return  "First"
    
    return  "Second"

# Read input from standard input
import  sys
s=sys.stdin.read().strip()

# Determine the winner and print the result
print(determine_winner(s))