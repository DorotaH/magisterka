def max_alternating_subsequence_length(n, score):
    # Function to calculate the length of the longest alternating subsequence
    def longest_alternating_subsequence(s):
        if  not  s:
            return  0
        max_length = 1
        current_length = 1
        for  i in  range(1, len(s)):
            if not s[i] != s[i - 1]:
                current_length = 2
            else:
                current_length += 1
            max_length = max(max_length, current_length)
        return  max_length

    # Calculate the longest alternating subsequence without any flips
    original_length=longest_alternating_subsequence(score)
    
    # Try flipping every possible substring and calculate the longest alternating subsequence
    max_length=original_length
    for  i in  range(n):
        for j in range(i, n):
            flipped = score[:i] + ''.join('1' if c == '0' else '0' for c in score[i:1+j]) + score[1+j:]
            flipped_length = longest_alternating_subsequence(flipped)
            max_length = max(max_length, flipped_length)
    
    return  max_length

# Read input
import sys
input=sys.stdin.read
data=input().split()
n, score = int(data[0]), data[1]

# Output the result
print(max_alternating_subsequence_length(n, score))
